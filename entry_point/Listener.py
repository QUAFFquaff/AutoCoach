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
    bar_signal = pyqtSignal([int, str])
    def __init__(self, eventQueue: multiprocessing.Queue, processLock: Lock, speed: Value, SVM_flag: Value, LDA_flag: Value):
        QThread.__init__(self)
        self.eventQueue = eventQueue
        self.processLock = processLock
        self.SVM_flag = SVM_flag
        self.ldamodel = LDAForEvent()



    def run(self):
        svm = joblib.load('svm.pkl')

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
                        # calculate the 17 features  To-Do
                        vect = self.calcData(vect)
                        # nomaliz the 17 features
                        vect = self.nomalization(vect)

                        result = svm.predict([vect])
                        score = svm.decision_function([vect])
                        score = np.array(score[0])

                        event_label = self.get_event_label(event_list[i], score)
                        level, type = self.get_level_type(event_label[0])
                        self.bar_signal[int, str].emit(level, type)


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