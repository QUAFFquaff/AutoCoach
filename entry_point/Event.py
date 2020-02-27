#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2/24/2020 10:16
# @File    : Event.py
# @Software: PyCharm

from GUI import *
from scipy import signal


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

    def get_starttime(self):
        return self.start

    def get_endtime(self):
        return self.end

    def get_duration(self):
        return self.end - self.start

    def get_type(self):
        return self.type

    def get_value(self):
        return self.vect

