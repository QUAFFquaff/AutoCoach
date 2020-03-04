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

from entry_point.LDA_scoreing import LDAForEvent

pattern = ['aa']
class LDAController(QThread):

    score_signal = pyqtSignal([int])
    def __init__(self, LDAbuffer):
        super().__init__()
        self.ldamodel = LDAForEvent("model")
        self.pattern = LDAbuffer
    def run(self) -> None:
        while True:
            start_time = datetime.datetime.now()
            score = self.score_pattern()
            end_time = datetime.datetime.now()
            print(end_time)
            dur = end_time - start_time
            time.sleep(20-dur.seconds)
            self.buffer = []
            self.pattern = ['a']
            print(self.pattern)

            self.score_signal.emit(score)

    def score_pattern(self):
        pattern = copy.deepcopy(self.pattern)
        self.pattern = []
        result = self.ldamodel.LDATest(pattern)
        score = self.ldamodel.score_pattern(result)
        return score

lda = LDAController(pattern)
lda.run()
print(pattern)