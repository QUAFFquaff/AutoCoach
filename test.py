import time

from PyQt5.QtCore import QThread
data = []

class Test1(QThread):
    def __init__(self):
        super().__init__()
        self.data =data

    def run(self):
        while True:
            print(self.data)
            self.data = []
            time.sleep(2)


class Test2(QThread):
    def __init__(self):
        super().__init__()
        self.data = data

    def run(self):
        while True:
            self.data.append('b')
            time.sleep(1)

test1 = Test1()
test2 = Test2()
test1.start()
test2.start()
while True:
    pass