#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2/24/2020 10:17
# @File    : DetectProcess2.py
# @Software: PyCharm


import time
import multiprocessing
from multiprocessing import *




class DetectProcess2(multiprocessing.Process):
    def __init__(self, eventQueue: multiprocessing.Queue, lock: Lock,speed: Value, svm_flag: Value, LDA_flag: Value):
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
