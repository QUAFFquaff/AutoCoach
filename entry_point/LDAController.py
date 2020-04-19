#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 3/2/2020 10:11
# @Author  : Haoyu Lyu
# @File    : LDAController.py
# @Software: PyCharm
import copy
import datetime
import time

from PyQt5.QtCore import QThread, pyqtSignal
from queue import Queue
from entry_point.LDA_scoreing import LDAForEvent
import threading

class LDAController(QThread):

    score_signal = pyqtSignal([int])
    def __init__(self, LDAbuffer ,feedback_queue:Queue, condition: threading.Condition):
        super().__init__()
        self.ldamodel = LDAForEvent("entry_point/model")
        self.pattern = LDAbuffer
        self.pattern_queue = feedback_queue
        self.condition = condition
    def run(self) -> None:
        with self.condition:
            while True:
                start_time = datetime.datetime.now()
                print(self.pattern)
                pattern_to_feedback = "".join(self.pattern)
                score = self.score_pattern()

                # communicate with feedback thread
                self.pattern_queue.put([pattern_to_feedback, score])
                if self.pattern_queue.full():  # notify feedback to poll all the 6 patterns
                    print("notify feedback thread")
                    self.condition.notify()
                    self.condition.wait()
                end_time = datetime.datetime.now()
                print(end_time)
                dur = end_time - start_time
                time.sleep(20-dur.seconds)

                self.score_signal.emit(score)

    def score_pattern(self):
        pattern = copy.deepcopy(self.pattern)
        print("copy:",pattern)
        while len(self.pattern)>0:
            self.pattern.remove(self.pattern[-1])
        result = self.ldamodel.LDATest(pattern)
        score = self.ldamodel.score_pattern(result)
        return score

# lda = LDAController(pattern)
# lda.run()
# print(pattern)