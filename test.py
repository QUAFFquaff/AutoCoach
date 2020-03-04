<<<<<<< HEAD
from scipy.stats import bernoulli
import matplotlib.pyplot as plt
import numpy as np
p = 0.5
temp = np.random.binomial(1,p,size=100)
x = []
for i in range(len(temp)):
    x.append(2 * temp[i] -1)
print(x)
y = [x[0]/2]
for i in range(1,len(x)):
    y.append((x[i]+x[i-1])/2)
z = [x[0]*2/3]
for i in range(1,len(x)):
    z.append( x[i] * 2/3 + x[i-1] / 3 )
print(y)
print('E[x] = ')
print(sum(x)/100)
print('E[y] = ')
print(sum(y)/100)
print('E[z] = ')
print(sum(z)/100)
=======
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
>>>>>>> 032d3190ae021784b995d3e26b43b1251627ed6f
