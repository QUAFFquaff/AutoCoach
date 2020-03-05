
from scipy.stats import bernoulli
import matplotlib.pyplot as plt
import numpy as np
from asyncio import sleep
from datetime import time

from PyQt5.QtCore import QThread

data = []


class Test1(QThread):
    def __init__(self, data1):
        super().__init__()
        self.data =data1

    def run(self):
        while True:
            self.data.append('a')
            print(self.data)


class Test2(QThread):
    def __init__(self, data2):
        super().__init__()
        self.data = data2

    def run(self):
        while True:
            self.data.append('b')

test1 = Test1(data)
test2 = Test2(data)
test1.start()
test2.start()
while True:
    pass

