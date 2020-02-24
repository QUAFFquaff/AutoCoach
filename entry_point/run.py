import sys
import os
from PyQt5.QtCore import pyqtSignal, QObject
from GUINext import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI import *
from QssLoader import *
import pyqtgraph as pg
import serial
import time
import multiprocessing
from ctypes import c_bool
import queue
from scipy import signal
from multiprocessing import *





class Event(object):
    def __init__(self, start_time: int, type: int):
        self.start = start_time
        self.type = type
        self.vect = []
        self.end = 0

    def set_endtime(self, end_time: int):
        self.end = end_time

    def add_value(self, data):
        self.vect.append(data)
        return self.vect

    def filter(self, b, a):
        temp = np.array(self.vect)
        temp = temp.astype(np.float64)
        y = signal.filtfilt(b, a, temp[:, 2])
        x = signal.filtfilt(b, a, temp[:, 3])
        z = signal.filtfilt(b, a, temp[:, 4])
        for i in range(0, len(temp)):
            self.vect[i][2] = y[i]
            self.vect[i][3] = x[i]
            self.vect[i][4] = z[i]

class detectProcess2(multiprocessing.Process):
    def __init__(self, eventQueue: multiprocessing.Queue, lock: Lock,speed: Value, svm_flag: Value):
        multiprocessing.Process.__init__(self)
        print('init')
        self.eventQueue = eventQueue
        self.processLock = lock
        self.speed = speed
        self.SVM_flag = svm_flag

    def run(self):
        while True:
            time.sleep(2)
            self.processLock.acquire()
            self.SVM_flag.value += 2
            self.eventQueue.put(0)
            self.processLock.release()

# process for event detection
class detectProcess(multiprocessing.Process):
    def __init__(self, eventQueue: multiprocessing.Queue, processLock: Lock, speed: Value, SVM_flag: Value):
        multiprocessing.Process.__init__(self, args=())
        print('init')
        self.eventQueue = eventQueue
        self.processLock = processLock
        self.speed = speed
        self.SVM_flag = SVM_flag
        # oriantation matrix
        self.matrix = np.array([[0.079935974, 0.00E+00, -0.9968],
                  [-0.993610238, 0.079, -0.079680179],
                  [0.079680205, 0.99687, 0.006389762]])
        # initial sampling rate and window for standard deviation calculation
        self.sampling_rate = 0
        self.std_window = 0

        # initial queue for standard deviation calculation
        self.std_x_queue = queue.Queue(maxsize=19)
        self.std_y_queue = queue.Queue(maxsize=19)
        self.acc_threshold_num = 0
        self.brake_threshold_num = 0
        self.acc_event = Event(0, 0)  # acc event object
        self.brake_event = Event(0, 1)  # brake event object
        self.acc_fault = 0  # fault left for acc
        self.brake_fault = 0  # fault left for brake


    def run(self):

        # initial obd connection
        self.bt_serial = self.getSerial()
        obd_data = ''.encode('utf-8')

        #initial sampling rate
        self.sampling_rate = self.getSamplingRate(obd_data)
        self.std_window = int(self.sampling_rate + 0.5)
        self.std_x_queue = queue.Queue(maxsize=(2 * self.std_window - 1))
        self.std_y_queue = queue.Queue(maxsize=(2 * self.std_window - 1))
        print('samplingrate--' + str(self.sampling_rate))
        print('std_window:', str(self.std_window))

        lowpass_queue = queue.Queue()
        cutoff = 2 * (1 / self.sampling_rate)  # cutoff frequency of low pass filter
        b, a = signal.butter(3, cutoff, 'low') # parameter for lowpass

        while True:
            row = obd_data + self.bt_serial.readline()
            row = self.splitByte(row)
            if row != "":
                timestamp = int(round(time.time()*1000))
                device_id = row[0]
                self.speed.value = row[1]
                acc_y = row[2]
                acc_x = row[3]
                acc_z = row[4]
                gyo_x = row[5]
                gyo_y = row[6]
                gyo_z = row[7]
                acc_list = np.array([acc_y, acc_x, acc_z])
                acc_list = acc_list.astype(np.float64)

                #calibration
                acc_list = np.dot(self.matrix, acc_list)
                lowpass_queue.put(acc_list)
                if lowpass_queue.qsize() > 59:
                    acc_x_filtered = signal.filtfilt(b, a, self.get_lowpass(lowpass_queue, 'x'))
                    acc_y_filtered = signal.filtfilt(b, a, self.get_lowpass(lowpass_queue, 'y'))
                    acc_z_filtered = signal.filtfilt(b, a, self.get_lowpass(lowpass_queue, 'z'))

                    # detect event
                    event_x = self.detect_x_event([timestamp, self.speed.value, acc_list[0], acc_list[1], acc_list[2], gyo_x, gyo_y, gyo_y, acc_y_filtered[-15], acc_x_filtered[-15], acc_z_filtered[-15]])
                    event_y = self.detect_x_event([timestamp, self.speed.value, acc_list[0], acc_list[1], acc_list[2], gyo_x, gyo_y, gyo_y, acc_y_filtered[-15], acc_x_filtered[-15], acc_z_filtered[-15]])

                    if not event_x is None:
                        event_x.filter(b, a)
                        self.processLock.acquire()  # get the lock
                        self.eventQueue.put(event_x)
                        self.SVM_flag.value -= 1
                        self.processLock.release()  # release the process lock
                        print("put acceleration or brake into svm")

                    lowpass_queue.get()
            else:
                print("something wrong with bluetooth")

    def getSerial(self):
        ser = serial.Serial(port='/dev/rfcomm0', baudrate=57600, timeout=0.5)
        if not ser.is_open:
            ser.open()
        return ser

    def getSamplingRate(self, obd_data):
        count_down = 15
        timestamp_list = []
        while count_down > 0:
            row = obd_data + self.bt_serial.readline()
            row = self.splitByte(row)
            if row!= "":
                timestamp_list.append(int(round(time.time()*1000)))
                count_down-=1
        sampling_rate = 14 / ((timestamp_list[-1]-timestamp_list[0])/1000)
        return sampling_rate

    def splitByte(self,obdData):
        row = obdData.split(b"\r")[0]
        row = row.split(b",")
        newrow = []
        if row != b"":
            if 9 > len(row) > 7:
                newrow.append(str(row[0], encoding="utf-8"))
                newrow.append(int(str(row[1], encoding="utf-8")))
                newrow.append(float(str(row[2], encoding="utf-8")))
                newrow.append(float(str(row[3], encoding="utf-8")))
                newrow.append(float(str(row[4], encoding="utf-8")))
                newrow.append(float(str(row[5], encoding="utf-8")))
                newrow.append(float(str(row[6], encoding="utf-8")))
                newrow.append(float(str(row[7], encoding="utf-8")))
            else:
                newrow = ""
        else:
            newrow = ""

        return newrow

    def get_lowpass(self, lowpass, opt):
        acc = []
        if opt == 'x':
            for i in range(lowpass.qsize()):
                temp = lowpass.get()
                lowpass.put(temp)
                acc.append(temp[1])
        if opt == 'y':
            for i in range(lowpass.qsize()):
                temp = lowpass.get()
                lowpass.put(temp)
                acc.append(temp[0])
        if opt == 'z':
            for i in range(lowpass.qsize()):
                temp = lowpass.get()
                lowpass.put(temp)
                acc.append(temp[2])

        return acc

    def change_event_num(self, num: int):
        self.processLock.acquire()
        self.SVM_flag += num
        self.processLock.release()

    def detect_x_event(self, data) -> Event:
        std_x_array = []
        raw_x_array = []
        acc_flag = False
        brake_flag = False
        fault_num = int(2 * self.sampling_rate / 5)  # fault tolerance
        min_event_length = int(self.sampling_rate * 1.2)  # minimum length for event

        self.std_x_queue.put(data)

        if self.std_x_queue.full():
            std_container = []
            for i in range(self.std_x_queue.qsize()):
                temp = self.std_x_queue.get()
                std_container.append(temp[9])
                if i >=self.std_window - 1:
                    std_x_array.append(np.std(std_container[i-self.std_window+1:i+1], ddof=1))
                    raw_x_array.append(temp[0:8])
                self.std_x_queue.put(temp)
            self.std_x_queue.get()  #delete current node
            start_index = std_x_array.index(min(std_x_array))

            std_x = std_x_array[-1]
            acc_x = data[9]
            timestamp = data[0]

            if acc_x > 0.12 and max(std_x_array) > 0.02 and self.acc_threshold_num == 0:  # if detect a new event
                self.acc_threshold_num += 1
                self.acc_event = Event(raw_x_array[start_index][0], 0)
                for i in range(start_index, len(raw_x_array)):
                    self.acc_event.add_value(raw_x_array[i])
                #  acquire process lock to add SVM_flag
                self.change_event_num(1)  # add 1 current event num
            elif acc_x > 0.06 and self.acc_threshold_num > 0:  # if event is continuing
                self.acc_threshold_num += 1
                self.acc_fault = fault_num
                acc_flag = True
            elif acc_x <= 0.06 and self.acc_fault > 0 and self.acc_threshold_num > 0:
                self.acc_fault -= 1
                self.acc_threshold_num += 1
                acc_flag = True
            elif (acc_x <= 0.06 or std_x < 0.01) and self.acc_threshold_num > 0:
                self.acc_fault = fault_num
                self.acc_threshold_num = 0
                if self.acc_threshold_num > min_event_length:
                    self.acc_event.set_endtime(timestamp)
                    self.acc_event.add_value(data[0:8])
                    return self.acc_event
                else:
                    #  acquire process lock to add SVM_flag
                    self.change_event_num(-1)  # minus 1 current event num


            if acc_x < -0.15 and max(std_x_array) > 0.02 and self.brake_threshold_num == 0:
                self.brake_threshold_num +=1
                self.brake_event = Event(std_x_array[start_index][0], 1)
                for i in range(start_index, len(std_x_array)):
                    self.brake_event.add_value(raw_x_array[i])
                #  acquire process lock to add SVM_flag
                self.change_event_num(1)  # add 1 current event num
            elif acc_x < -0.06 and self.brake_threshold_num > 0:
                self.brake_threshold_num += 1
                self.brake_fault = fault_num
                brake_flag = True
            elif acc_x >= -0.06 and self.brake_fault > 0 and self.brake_threshold_num > 0:
                self.brake_fault -= 1
                self.brake_threshold_num += 1
                brake_flag = True
            elif (acc_x >= -0.06 or std_x < 0.01) and self.brake_threshold_num >0:
                self.brake_threshold_num = 0
                self.brake_fault = fault_num
                if self.brake_threshold_num > min_event_length:
                    self.brake_event.set_endtime(timestamp)
                    self.brake_event.add_value(data[0:8])
                    return self.brake_event
                else:
                    #  acquire process lock to add SVM_flag
                    self.change_event_num(-1)  # minus 1 current event num

            if acc_flag:
                self.acc_event.add_value(data[0:8])
            if brake_flag:
                self.brake_event.add_value(data[0:8])






class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        styleFile = '././QSS/style.qss'
        qssStyle = QssLoader.loadQss(styleFile)
        self.setStyleSheet(qssStyle)

        # initial class for next page
        self.nextWin = NextWindow()

        # bind show function to button
        self.next_page.clicked.connect(self.showNext)
        self.total_score.clicked.connect(self.showNext)
        self.nextWin.backSignal.connect(self.showMain)

    def showMain(self):
        self.setVisible(True)

    def showNext(self):
        self.setVisible(False)
        self.nextWin.setVisible(True)


class NextWindow(QMainWindow, Ui_Dialog):
    backSignal = pyqtSignal()

    def __init__(self):
        super(NextWindow, self).__init__()
        self.setupUi(self)

        styleFile = '././QSS/style_next.qss'
        qssStyle = QssLoader.loadQss(styleFile)
        self.setStyleSheet(qssStyle)

        # bind back button
        self.backBtn.clicked.connect(self.backMain)

    def backMain(self):
        self.backSignal.emit()
        self.setVisible(False)


class ListenerThread(QThread):
    back_signal = pyqtSignal(int)
    def __init__(self, parent=None, args=()):
        super(ListenerThread, self).__init__(parent)
        self.eventQueue = args[0]
        self.processLock = args[1]
        self.SVM_flag = args[2]

    def run(self):
        i = 0
        while True:
            print(self.SVM_flag.value)

            i +=1
            if not self.eventQueue.empty():
                score = self.eventQueue.get()

                self.back_signal.emit(score)





def run():
    eventQueue = multiprocessing.Queue()
    processLock = multiprocessing.Lock()
    speed = multiprocessing.Value("i", 0)
    SVM_flag = multiprocessing.Value("i", 0)
    LDA_flag = multiprocessing.Value(c_bool, True)

    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()




    timer = pg.QtCore.QTimer()
    timer.timeout.connect(myWin.update2)
    timer.start(50)

    eventDetectP = detectProcess2(eventQueue, processLock, speed, SVM_flag)
    eventDetectP.daemon = True
    eventDetectP.start()

    listener = ListenerThread(args=(eventQueue, processLock, SVM_flag))
    listener.back_signal.connect(myWin.setCurrentScore)
    listener.start()

    myWin.setCurrentScore(45)
    myWin.setFeedBack(1,'acc')


    myWin.setBar('safe','acc')
    myWin.setBar('mediumrisk','brake')
    myWin.setBar('highrisk','turn')
    myWin.setBar('safe','swerve')


    sys.exit(app.exec_())

