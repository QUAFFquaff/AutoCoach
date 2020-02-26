from entry_point.DetectProcess2 import *
from entry_point.DetectProcess import *
from entry_point.Event import *
import joblib
import numpy as np



class ListenerThread(QThread):
    back_signal = pyqtSignal(int)
    def __init__(self, eventQueue: multiprocessing.Queue, processLock: Lock, speed: Value, SVM_flag: Value, LDA_flag: Value):
        QThread.__init__(self)
        self.eventQueue = eventQueue
        self.processLock = processLock
        self.SVM_flag = SVM_flag

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

            # print(self.SVM_flag.value)
            #
            # i +=1
            # if not self.eventQueue.empty():
            #     score = self.eventQueue.get()
            #
            #     self.back_signal.emit(score)

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
        max = [0.7614, 0.6011, 0.2729, 0.2104, 11.510, 4.6303, 0.2529, 0.2861, 13.922, 1.6740, 31.65, 0.51791,
               0.54475, 0.1544, 0.0674, 75.0, 94.7125, 29.1634, 17.16]
        min = [0.06909, 0.0079, 0.0206, 0.0020, 0.3709, 0.7642, -0.356, -0.277, -16.325, -2.0252, 2.27, -0.0867,
               -0.0405, -0.748, -0.589, -90.0, 2.67796, 0.40508, 1.848]
        for i in range(len(vect)):
            vect[i] = (vect[i] - min[i]) / (max[i] - min[i])
        return vect