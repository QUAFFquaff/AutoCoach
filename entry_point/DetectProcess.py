#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2/24/2020 10:18
# @Author  : Haoyu Lyu
# @File    : DetectProcess.py
# @Software: PyCharm

from GUI import *
import serial
import time
import multiprocessing
from queue import Queue
from scipy import signal
from multiprocessing import *
from entry_point.Event import Event


# process for event detection
class DetectProcess(multiprocessing.Process):
    def __init__(self, eventQueue: multiprocessing.Queue, processLock: Lock, speed: Value, SVM_flag: Value, LDA_flag: Value):
        multiprocessing.Process.__init__(self)
        print('init event detection')
        self.eventQueue = eventQueue
        self.processLock = processLock
        self.speed = speed
        self.SVM_flag = SVM_flag
        self.LDA_flag = LDA_flag
        # oriantation matrix
        self.matrix = np.array([[-0.22220486, 0.00E+00, 0.975],
                  [0.974561151, -0.03, 0.222104846],
                  [0.02925, 0.999549899, 0.006666146]])
        # initial sampling rate and window for standard deviation calculation
        self.sampling_rate = 0
        self.std_window = 0

        # initial queue for standard deviation calculation
        self.std_x_queue = Queue(maxsize=19)
        self.std_y_queue = Queue(maxsize=19)
        self.acc_threshold_num = 0
        self.brake_threshold_num = 0
        self.acc_event = Event(0, 0)  # acc event object
        self.brake_event = Event(0, 1)  # brake event object
        self.acc_fault = 0  # fault left for acc
        self.brake_fault = 0  # fault left for brake

        self.turn_threshold_num = 0
        self.y_positive = True
        self.y_negative = True
        self.turn_event = Event(0, 2)
        self.swerve_event = Event(0, 3)
        self.turn_fault = 0

    def run(self):

        # initial obd connection
        self.bt_serial = self.getSerial()
        obd_data = ''.encode('utf-8')

        #initial sampling rate
        self.sampling_rate = self.getSamplingRate(obd_data)
        self.std_window = int(self.sampling_rate + 0.5)
        self.std_x_queue = Queue(maxsize=(2 * self.std_window - 1))
        self.std_y_queue = Queue(maxsize=(2 * self.std_window - 1))
        print('samplingrate--' + str(self.sampling_rate))
        print('std_window:', str(self.std_window))

        lowpass_queue = Queue()
        data_buffer = Queue(maxsize=6)
        cutoff = 2 * (1 / self.sampling_rate)  # cutoff frequency of low pass filter
        b, a = signal.butter(3, cutoff, 'low')  # parameter for lowpass

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
                if data_buffer.full():
                    data_buffer.get()
                data_buffer.put(np.array([timestamp, self.speed.value, acc_y, acc_x, acc_z, gyo_x, gyo_y, gyo_z]))
                if lowpass_queue.qsize() > 59:
                    acc_x_filtered = signal.filtfilt(b, a, self.get_lowpass(lowpass_queue, 'x'))
                    acc_y_filtered = signal.filtfilt(b, a, self.get_lowpass(lowpass_queue, 'y'))
                    acc_z_filtered = signal.filtfilt(b, a, self.get_lowpass(lowpass_queue, 'z'))
                    event_data = data_buffer.get()

                    # detect event
                    event_x = self.detect_x_event([event_data[0], event_data[1], event_data[2], event_data[3], event_data[4], event_data[5], event_data[6], event_data[7], 0, acc_y_filtered[-6], acc_x_filtered[-6], acc_z_filtered[-6]])
                    event_y = self.detect_y_event([event_data[0], event_data[1], event_data[2], event_data[3], event_data[4], event_data[5], event_data[6], event_data[7], 1, acc_y_filtered[-6], acc_x_filtered[-6], acc_z_filtered[-6]])

                    if event_x is not None:
                        print("there is a event from x axis")
                        event_x.filter(b, a)
                        self.processLock.acquire()  # get the lock
                        self.eventQueue.put(event_x)
                        self.SVM_flag.value -= 1
                        self.processLock.release()  # release the process lock
                        print("put acceleration or brake into svm")
                    if event_y is not None:
                        print("there is a event from yaxis")
                        event_y.filter(b, a)
                        self.processLock.acquire()  # get the lock
                        self.eventQueue.put(event_y)
                        self.SVM_flag.value -= 1
                        self.processLock.release()  # release the process lock
                        print("put turn into svm")

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
        self.SVM_flag.value += num
        self.processLock.release()

    def detect_x_event(self, data) -> Event:
        #print(data)
        std_x_array = []
        raw_x_array = []
        acc_flag = False
        brake_flag = False
        fault_num = int(1 * self.sampling_rate / 5)  # fault tolerance
        min_event_length = int(self.sampling_rate * 0.4)  # minimum length for event

        self.std_x_queue.put(data)

        if self.std_x_queue.full():
            std_container = []
            for i in range(self.std_x_queue.qsize()):
                temp = self.std_x_queue.get()
                std_container.append(temp[10])
                if i >=self.std_window - 1:
                    std_x_array.append(np.std(std_container[i-self.std_window+1:i+1], ddof=1))
                    raw_x_array.append(temp[0:9])
                self.std_x_queue.put(temp)
            self.std_x_queue.get()  #delete current node
            start_index = std_x_array.index(min(std_x_array))

            std_x = std_x_array[-1]
            acc_x = data[10]
            timestamp = data[0]

            if acc_x > 0.08 and max(std_x_array) > 0.02 and self.acc_threshold_num == 0:  # if detect a new event
                print("acc event start")
                self.acc_threshold_num += 1
                self.acc_event = Event(raw_x_array[start_index][0], 0)
                for i in range(start_index, len(raw_x_array)):
                    self.acc_event.add_value(raw_x_array[i])
                #  acquire process lock to add SVM_flag
                self.change_event_num(1)  # add 1 current event num
            elif acc_x > 0.04 and self.acc_threshold_num > 0:  # if event is continuing
                self.acc_threshold_num += 1
                self.acc_fault = fault_num
                acc_flag = True
            elif acc_x <= 0.04 and self.acc_fault > 0 and self.acc_threshold_num > 0:
                self.acc_fault -= 1
                self.acc_threshold_num += 1
                acc_flag = True
            elif (acc_x <= 0.04 or std_x < 0.01) and self.acc_threshold_num > 0:
                self.acc_fault = fault_num
                
                if self.acc_threshold_num > min_event_length:
                    print("there is acc event end")
                    self.acc_event.set_endtime(timestamp)
                    self.acc_event.add_value(data[0:9])
                    self.acc_threshold_num = 0
                    return self.acc_event
                else:
                    self.acc_threshold_num = 0
                    print(" acc event cancel")
                    #  acquire process lock to add SVM_flag
                    self.change_event_num(-1)  # minus 1 current event num


            if acc_x < -0.08 and max(std_x_array) > 0.02 and self.brake_threshold_num == 0:
                print("brake event start")
                self.brake_threshold_num +=1
                self.brake_event = Event(raw_x_array[start_index][0], 1)
                for i in range(start_index, len(raw_x_array)):
                    self.brake_event.add_value(raw_x_array[i])
                #  acquire process lock to add SVM_flag
                self.change_event_num(1)  # add 1 current event num
            elif acc_x < -0.04 and self.brake_threshold_num > 0:
                self.brake_threshold_num += 1
                self.brake_fault = fault_num
                brake_flag = True
            elif acc_x >= -0.04 and self.brake_fault > 0 and self.brake_threshold_num > 0:
                self.brake_fault -= 1
                self.brake_threshold_num += 1
                brake_flag = True
            elif (acc_x >= -0.04 or std_x < 0.01) and self.brake_threshold_num >0:
                
                self.brake_fault = fault_num
                if self.brake_threshold_num > min_event_length:
                    print("brake event end")
                    self.brake_event.set_endtime(timestamp)
                    self.brake_event.add_value(data[0:9])
                    self.brake_threshold_num = 0
                    return self.brake_event
                else:
                    self.brake_threshold_num = 0
                    print("brake event cancel")
                    #  acquire process lock to add SVM_flag
                    self.change_event_num(-1)  # minus 1 current event num

            if acc_flag:
                self.acc_event.add_value(data[0:9])
            if brake_flag:
                self.brake_event.add_value(data[0:9])

    def detect_y_event(self, data) -> Event:
        std_y_array = []
        raw_y_array = []
        flag = False
        min_length = int(self.sampling_rate)
        max_length = int(self.sampling_rate * 14)
        fault_num = int(2 * self.sampling_rate / 10)
        self.std_y_queue.put(data)

        if self.std_y_queue.full():
            std_container = []
            for i in range(self.std_y_queue.qsize()):
                temp = self.std_y_queue.get()
                std_container.append(temp[9])
                if i >= self.std_window - 1:
                    std_y_array.append(np.std(std_container[i - self.std_window + 1:i + 1], ddof=1))
                    raw_y_array.append(temp[0:9])
                self.std_y_queue.put(temp)
            self.std_y_queue.get()  # delete current node
            start_index = std_y_array.index(min(std_y_array))

            std_y = std_y_array[-1]
            acc_y = data[8]
            timestamp = data[0]

            if self.y_positive:
                if acc_y > 0.15 and max(std_y_array) > 0.015 and self.turn_threshold_num == 0:
                    #print("left start")
                    self.turn_threshold_num += 1
                    self.turn_event = Event(raw_y_array[start_index][0], 2)
                    for i in range(start_index, len(std_y_array)):
                        self.turn_event.add_value(raw_y_array[i])
                    #  acquire process lock to add SVM_flag
                    self.change_event_num(1)  # add 1 current event num
                    self.y_negative = False
                elif acc_y > 0.06 and self.turn_threshold_num > 0:
                    self.turn_threshold_num += 1
                    self.turn_fault = fault_num
                    flag = True
                elif acc_y <=0.06 and self.turn_fault > 0 and self.turn_threshold_num > 0:
                    self.turn_fault -= 1
                    self.turn_threshold_num += 1
                    flag = True
                elif (acc_y <= 0.06 or std_y < 0.015) and self.turn_threshold_num > 0:
                    
                    self.turn_fault = 0
                    self.y_negative = True
                    if min_length < self.turn_threshold_num < max_length:
                        print("left turn ends")
                        self.turn_event.set_endtime(timestamp)
                        self.turn_event.add_value(data[0:9])
                        self.turn_threshold_num = 0
                        return self.turn_event
                    else:
                        #print("left turn cancel")
                        self.turn_threshold_num = 0
                        self.change_event_num(-1)

            if self.y_negative:
                if acc_y < -0.15 and max(std_y_array) > 0.015 and self.turn_threshold_num == 0:
                    #print("right trun start")
                    self.turn_threshold_num += 1
                    self.turn_event = Event(raw_y_array[start_index][0], 3)
                    for i in range(start_index, len(std_y_array)):
                        self.turn_event.add_value(raw_y_array[i])
                    #  acquire process lock to add SVM_flag
                    self.change_event_num(1)  # add 1 current event num
                    self.y_positive = False
                elif acc_y < -0.06 and self.turn_threshold_num > 0:
                    self.turn_threshold_num += 1
                    self.turn_fault = fault_num
                    flag = True
                elif acc_y >= -0.06 and self.turn_fault > 0 and self.turn_threshold_num > 0:
                    self.turn_fault -= 1
                    self.turn_threshold_num += 1
                    flag = True
                elif (acc_y >= -0.06 or std_y < 0.015) and self.turn_threshold_num > 0:
                    
                    self.turn_fault = 0
                    self.y_positive = True
                    if min_length < self.turn_threshold_num < max_length:
                        print("right turn ends")
                        self.turn_event.set_endtime(timestamp)
                        self.turn_event.add_value(data[0:9])
                        self.turn_threshold_num = 0
                        return self.turn_event
                    else:
                        #print("right cancel")
                        self.turn_threshold_num = 0
                        self.change_event_num(-1)

            if flag:
                self.turn_event.add_value(data[0:9])



