from asyncio import sleep
from datetime import time

from PyQt5.QtCore import QThread

data = []


class Test1(QThread):
    def __init__(self):
        super().__init__()
        self.data =data
        self.data.append('a')

    def run(self):
        while True:
            self.data.append('a')
            print(self.data)


class Test2(QThread):
    def __init__(self):
        super().__init__()
        self.data = data

    def run(self):
        while True:
            self.data.append('b')

test1 = Test1()
test2 = Test2()
test1.start()
test2.start()
while True:
    pass