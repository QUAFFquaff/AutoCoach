
from asyncio import sleep
from datetime import time
import time
from PyQt5.QtCore import QThread
import copy
data = []



# class Test1(QThread):
#     def __init__(self, data1):
#         super().__init__()
#         self.dat =data1
#
#     def run(self):
#         while True:
#             pattern = copy.deepcopy(self.dat)
#             print(pattern)
#             time.sleep(1)
#             # while len(self.dat)>0:
#             self.dat.remove(self.dat[-1])
#
#
# class Test2(QThread):
#     def __init__(self, data2):
#         super().__init__()
#         self.data = data2
#
#     def run(self):
#         while True:
#             self.data.append('b')
#             time.sleep(1)
#
# test1 = Test1(data)
# test2 = Test2(data)
# test1.start()
# test2.start()
# while True:
#     pass


event_mid_dict = {'i': 0, 'b': 0, 'p': 0, 'w': 0}
event_high_dict = {'j': 0, 'c': 0, 'q': 0, 'x': 0}
max_high = max(event_high_dict, key=event_high_dict.get)
print(max_high)

data = [0,1,2,3,4,5,6,7,8,9,10]
print(data[0:9])


