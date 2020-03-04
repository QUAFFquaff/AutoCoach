# from entry_point.DetectProcess2 import *
# from entry_point.DetectProcess import *
import multiprocessing
from multiprocessing import *
from entry_point.Event import Event
import numpy as np
from PyQt5.QtCore import pyqtSignal, QThread

from entry_point.LDA_scoreing import LDAForEvent
import joblib


class ListenerThread(QThread):
    bar_signal = pyqtSignal(int, str)
    score_signal = pyqtSignal(int)
    def __init__(self, eventQueue: multiprocessing.Queue, processLock: Lock, speed: Value, SVM_flag: Value, LDA_buffer: list):
        QThread.__init__(self)
        self.eventQueue = eventQueue
        self.processLock = processLock
        self.SVM_flag = SVM_flag
        self.buffer = LDA_buffer
        self.svm = joblib.load('svm.pkl')




    def run(self):
        while True:

            if (not self.eventQueue.empty()) and self.SVM_flag.value == 0:
                event_list = []
                while(not self.eventQueue.empty()):
                    event_list.append(self.eventQueue.get())
                event_list = self.makeDecision(event_list)

                for i in range(0, len(event_list)):
                    if event_list[i] is not None:
                        vect = np.array(event_list[i].getValue())
                        vect = vect.astype(np.float64)
                        # function name: calculate_feature()
                        # calculate the 17 features
                        # @param: vect[timestamp, speed, acc_y, acc_x, acc_z, gyo_x, gyo_y, gyo_z, axis(0 or 1)]
                        # To-Do
                        vect = self.calculate_feature(vect)
                        # nomaliz the 17 features
                        vect = self.nomalization(vect)

                        result = self.svm.predict([vect])
                        score = self.svm.decision_function([vect])
                        score = np.array(score[0])

                        event_label = self.get_event_label(event_list[i], score)
                        level, type = self.get_level_type(event_label[0])

                        self.bar_signal.emit(level, type)

                        # emit pattern score to ui
                        self.bar_signal[int].emit(score)
                        self.buffer.append(type)



    def calculate_feature(self,vect):
        maxAX = max(vect[:, 3])
        maxAY = max(vect[:, 2])
        minAX = min(vect[:, 3])
        minAY = min(vect[:, 2])
        maxAccX = max(abs(vect[:, 3]))
        maxAccY = max(abs(vect[:, 2]))
        datalist = vect[:, 3].tolist()
        # print(datalist.index(max(datalist)))
        fraction = datalist.index(max(datalist)) / len(datalist)

        rangeAX = maxAX - minAX
        rangeAY = maxAY - minAY

        varAX = np.std(vect[:, 3])
        varAY = np.std(vect[:, 2])
        meanAX = np.mean(vect[:, 3])
        meanAY = np.mean(vect[:, 2])
        meanOX = np.mean(vect[:, 5])
        maxOX = max(abs(vect[:, 5]))
        maxOY = max(abs(vect[:, 6]))
        maxOri = max(maxOX, maxOY)
        t = (vect[-1, 1] - vect[0, 1]) / 1000
        meanSP = np.mean(vect[:, 1])
        differenceSP = vect[-1, 1] - vect[0, 1]
        accelerate = differenceSP / t
        varSP = np.std(vect[:, 1])
        StartEndAccx = vect[0, 3] + vect[-1, 3]
        StartEndAccy = vect[0, 2] + vect[-1, 2]
        axis = vect[0, -1]
        return [rangeAX, rangeAY, varAX, varAY, meanAX, meanAY, meanOX, maxOri, maxAX, minAX, maxAccY, differenceSP,
                meanSP, StartEndAccx, StartEndAccy, t, axis]  # 99% 86%

    def get_level_type(self, label):
        type = ""
        if label<3:
            type = "acc"
        elif 2<label<6:
            type = "brake"
        elif 5<label<9:
            type = "turn"
        elif 8<label<12:
            type = "swerve"

        return (label % 3), type

    def get_event_label(self, event, score):
        result = [0]
        if event.getType() >= 2:
            index = np.argmax([score[2], score[3], score[6], score[7], score[10], score[11]])
            if index == 0:
                result = [2]
            elif index == 1:
                result = [3]
            elif index == 2:
                result = [6]
            elif index == 3:
                result = [7]
            elif index == 4:
                result = [10]
            else:
                result = [11]
        elif event.getType() == 0:
            index = np.argmax([score[0], score[4], score[8]])
            if index == 0:
                result = [0]
            elif index == 1:
                result = [4]
            elif index == 2:
                result = [8]
        elif event.getType() == 1:
            index = np.argmax([score[1], score[5], score[9]])
            if index == 0:
                result = [1]
            elif index == 1:
                result = [5]
            elif index == 2:
                result = [9]
        return result

    def makeDecision(self, event_list):
        for i in range(0, len(event_list)-1):
            if event_list[i]:
                factor1 = (event_list[i].get_endtime() - event_list[i + 1].get_starttime()) / event_list[i].get_duration()
                factor2 = (event_list[i + 1].get_endtime() - event_list[i].get_endtime()) / event_list[i + 1].get_duration()
                if factor1 > 0.5 and factor2 < 0.5:
                    if event_list[i].get_type() >= 2 > event_list[i + 1].get_type():
                        event_list[i + 1] = None
                    elif event_list[i].get_type() < 2 <= event_list[i + 1].get_type():
                        event_list[i] = None
        return event_list

    def nomalization(self, vect):
        max = [0.54477258, 0.50700942, 0.18789488, 0.15918743, 0.24768464, 0.23842632, 28.50689189, 74.8, 0.49226227, 0.15066697, 0.51110881, 70.,
               123.13157895, 0.4805202, 0.33492619, 16.691, 1.]
        min = [2.35382837e-02, 3.20113117e-02, 9.27135340e-03, 1.15892844e-02, -3.15876755e-01, -2.84492464e-01, -2.16178814e+01, 3.39000000e+00, -1.93298970e-01, -5.84772122e-01, 3.08761631e-02, -7.20000000e+01,
               2.14285714e-01, -5.22672514e-01, -2.49833594e-01, 8.72000000e-01, 0.]
        for i in range(len(vect)):
            vect[i] = (vect[i] - min[i]) / (max[i] - min[i])
        return vect

    def score_pattern(self,pattern):

        result = self.ldamodel.LDATest(pattern)
        print(self.ldamodel.score_pattern(result))