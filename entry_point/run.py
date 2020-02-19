import sys
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
    def __init__(self,args=()):
        multiprocessing.Process.__init__(self)
        print('init')

    def run(self):
        print('run')
        while True:
            print('running')




class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

        styleFile = '././QSS/style.qss'
        qssStyle = QssLoader.loadQss(styleFile)
        self.setStyleSheet(qssStyle)



def run():
    app = QApplication(sys.argv)
    myWin = MyWindow()

    myWin.show()

    timer = pg.QtCore.QTimer()
    timer.timeout.connect(myWin.update2)
    timer.start(50)

    eventDetectP = detectProcess(args=(myWin,))
    eventDetectP.daemon = True
    eventDetectP.start()

    myWin.setFeedBack(1,'acc')
    # myWin.setFeedBack(0,'acc')
    # myWin.setFeedBack(0,'brake')
    # myWin.setFeedBack(2,'brake')


    sys.exit(app.exec_())

