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
    update_score = pyqtSignal([int])
    def __init__(self):
        multiprocessing.Process.__init__(self)
        print('init')

    def run(self):
        i=0
        while True:
            time.sleep(2)
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
        self.TotalScore.clicked.connect(self.showNext)
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



def run():
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()




    timer = pg.QtCore.QTimer()
    timer.timeout.connect(myWin.update2)
    timer.start(50)

    eventDetectP = detectProcess()
    eventDetectP.daemon = True
    eventDetectP.start()

    myWin.setCurrentScore(45)
    myWin.setFeedBack(1,'acc')
    # myWin.setFeedBack(0,'acc')
    # myWin.setFeedBack(0,'brake')
    # myWin.setFeedBack(2,'brake')


    sys.exit(app.exec_())

