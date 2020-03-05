
from asyncio import sleep
from datetime import time
import time
from PyQt5.QtCore import QThread

data = []


class Test2(QThread):
    def __init__(self, data2:list):
        super().__init__()
        self.dat = data2

    def run(self):
        while True:
            # self.dat.append('b')
            pattern = copy.deepcopy(self.dat)
            print(pattern)
            time.sleep(1)
            while len(self.dat)>0:
                self.dat.remove(self.dat[-1])


class Test1(QThread):
    def __init__(self,data1:list):
        super().__init__()
        self.data1 =data1
        # self.data.append('a')

    def run(self):
        while True:
            self.data1.append('a')
            print(self.data1)
            time.sleep(1)





def run():
    test1 = Test1(data)
    test2 = Test2(data)
    test1.start()
    test2.start()
    while True:
        pass

