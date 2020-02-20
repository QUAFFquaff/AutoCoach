import sys
import os
from PyQt5.QtCore import pyqtSignal, QObject
from GUINext import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI import *
from QssLoader import *
import pyqtgraph as pg
import serial
import time
import multiprocessing



def getSerial():
    ser = serial.Serial(port='/dev/rfcomm0', baudrate=57600, timeout=0.5)
    if not ser.is_open:
        ser.open()
    return ser


class detectProcess(multiprocessing.Process):
    def __init__(self, args=()):
        multiprocessing.Process.__init__(self, args=())
        print('init')
        self.eventQueue = args[0]
        self.processLock = args[1]

    def run(self):
        i=0
        while True:
            time.sleep(1)
            self.processLock.acquire()
            self.eventQueue.put(i)
            self.processLock.release()
            print('process' + str(self.eventQueue.qsize()))
            i = i+1
            print('running')


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        styleFile = '././QSS/style.qss'
        qssStyle = QssLoader.loadQss(styleFile)
        self.setStyleSheet(qssStyle)

        # initial class for next page
        self.nextWin = NextWindow()

        # bind show function to button
        self.next_page.clicked.connect(self.showNext)
        self.total_score.clicked.connect(self.showNext)
        self.nextWin.backSignal.connect(self.showMain)

    def showMain(self):
        self.setVisible(True)

    def showNext(self):
        self.setVisible(False)
        self.nextWin.setVisible(True)


class NextWindow(QMainWindow, Ui_Dialog):
    backSignal = pyqtSignal()

    def __init__(self):
        super(NextWindow, self).__init__()
        self.setupUi(self)

        styleFile = '././QSS/style_next.qss'
        qssStyle = QssLoader.loadQss(styleFile)
        self.setStyleSheet(qssStyle)

        # bind back button
        self.backBtn.clicked.connect(self.backMain)

    def backMain(self):
        self.backSignal.emit()
        self.setVisible(False)


class ListenerThread(QThread):
    back_signal = pyqtSignal(int)
    def __init__(self, parent=None, args=()):
        super(ListenerThread, self).__init__(parent)
        self.eventQueue = args[0]

    def run(self):
        count_down = 15
        while True:
            time.sleep(1)
            print(self.eventQueue.qsize())

            if not self.eventQueue.empty():
                score = self.eventQueue.get()

                self.back_signal.emit(score)





def run():
    eventQueue = multiprocessing.Queue()
    processLock = multiprocessing.Lock()

    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()




    timer = pg.QtCore.QTimer()
    timer.timeout.connect(myWin.update2)
    timer.start(50)

    eventDetectP = detectProcess(args=(eventQueue,processLock,))
    eventDetectP.daemon = True
    eventDetectP.start()

    listener = ListenerThread(args=(eventQueue,))
    listener.back_signal.connect(myWin.setCurrentScore)
    listener.start()

    myWin.setCurrentScore(45)
    myWin.setFeedBack(1,'acc')


    myWin.setBar('safe','acc')
    myWin.setBar('mediumrisk','brake')
    myWin.setBar('highrisk','turn')
    myWin.setBar('safe','swerve')


    sys.exit(app.exec_())

