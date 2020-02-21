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
import queue
from scipy import signal



# initial queue for standard deviation calculation
std_x_queue = queue.Queue(maxsize=19)
std_y_queue = queue.Queue(maxsize=19)



# process for event detection
class detectProcess(multiprocessing.Process):
    def __init__(self, args=()):
        multiprocessing.Process.__init__(self, args=())
        print('init')
        self.eventQueue = args[0]
        self.processLock = args[1]
        self.speed = args[2]
        # oriantation matrix
        self.matrix = np.array([[0.079935974, 0.00E+00, -0.9968],
                  [-0.993610238, 0.079, -0.079680179],
                  [0.079680205, 0.99687, 0.006389762]])
        # initial sampling rate and window for standard deviation calculation
        self.sampling_rate = 0
        self.std_window = 0

    def run(self):

        # initial obd connection
        self.bt_serial = self.getSerial()
        obd_data = ''.encode('utf-8')

        #initial sampling rate
        self.sampling_rate = self.getSamplingRate(obd_data)
        self.std_window = int(self.sampling_rate + 0.5)
        std_x_queue = queue.Queue(maxsize=(2 * self.std_window - 1))
        std_y_queue = queue.Queue(maxsize=(2 * self.std_window - 1))
        print('samplingrate--' + str(self.sampling_rate))
        print('std_window:', str(self.std_window))

        lowpass_count = 0
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
                lowpass_count += 1
                if(lowpass_count > 59):
                    acc_x_filtered = signal.filtfilt(b, a, self.get_lowpass(lowpass_queue, 'x'))
                    acc_y_filtered = signal.filtfilt(b, a, self.get_lowpass(lowpass_queue, 'y'))
                    acc_z_filtered = signal.filtfilt(b, a, self.get_lowpass(lowpass_queue, 'z'))

                    # detect event
                    event_x = self.detect_x_event([timestamp, self.speed.value, acc_y_filtered[-4], acc_x_filtered[-4], acc_z_filtered[-4], gyo_x, gyo_y, gyo_y])
                    event_y = self.detect_x_event([timestamp, self.speed.value, acc_y_filtered[-4], acc_x_filtered[-4], acc_z_filtered[-4], gyo_x, gyo_y, gyo_y])



            time.sleep(1)
            self.processLock.acquire()
            self.eventQueue.put(i)
            self.processLock.release()
            print('process' + str(self.eventQueue.qsize()))
            i = i+1
            print('running')

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

    def detect_x_event(self, data):
        faultNum = int(2 * self.sampling_rate / 5)
        min_event_length = int(self.sampling_rate * 1.2)

        std_x_queue.put(data)




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

    def run(self):
        i = 0
        while True:
            time.sleep(1)
            print(self.eventQueue.qsize())
            self.eventQueue.put(i)
            i +=1
            if not self.eventQueue.empty():
                score = self.eventQueue.get()

                self.back_signal.emit(score)





def run():
    eventQueue = multiprocessing.Queue()
    processLock = multiprocessing.Lock()
    speed = multiprocessing.Value("i", 0)

    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()




    timer = pg.QtCore.QTimer()
    timer.timeout.connect(myWin.update2)
    timer.start(50)

    # eventDetectP = detectProcess(args=(eventQueue, processLock, speed,))
    # eventDetectP.daemon = True
    # eventDetectP.start()

    listener = ListenerThread(args=(eventQueue,))
    listener.back_signal.connect(myWin.setCurrentScore)
    listener.start()

    myWin.setCurrentScore(45)
    myWin.setFeedBack(1,'acc')


    myWin.setBar('safe','acc')
    myWin.setBar('mediumrisk','brake')
    myWin.setBar('highrisk','turn')
    myWin.setBar('safe','swerve')


    sys.exit(app.exec_())

