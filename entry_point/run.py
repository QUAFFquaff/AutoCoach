
from entry_point.DetectProcess import DetectProcess
from entry_point.Event import Event
from entry_point.LDAController import LDAController
from entry_point.Listener import ListenerThread
import sys
from PyQt5.QtCore import pyqtSignal
from GUINext import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI import *
from QssLoader import *
import pyqtgraph as pg
import multiprocessing
from ctypes import c_bool
import threading
from entry_point.FeedbackController import FeedbackController
from queue import Queue


LDA_buffer = []

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
    global LDA_buffer
    eventQueue = multiprocessing.Queue()
    processLock = multiprocessing.Lock()
    speed = multiprocessing.Value("i", 0)
    SVM_flag = multiprocessing.Value("i", 0)
    LDA_flag = multiprocessing.Value(c_bool, True)

    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()

    timer = pg.QtCore.QTimer()
    timer.timeout.connect(myWin.update_flowing_score)
    timer.start(400)

    eventDetectP = DetectProcess(eventQueue, processLock, SVM_flag, LDA_flag)
    eventDetectP.daemon = True
    eventDetectP.start()

    listener = ListenerThread(eventQueue, processLock, SVM_flag, LDA_buffer)
    listener.bar_signal.connect(myWin.setBar)
    listener.start()

    cond = threading.Condition()
    feedback_queue = Queue(maxsize=1)
    feedback_controller = FeedbackController(feedback_queue, cond)
    feedback_controller.daemon = True
    feedback_controller.feedback_signal.connect(myWin.setFeedBack)
    feedback_controller.start()

    lda_controller = LDAController(LDA_buffer, feedback_queue, cond)
    lda_controller.score_signal.connect(myWin.setCurrentScore)
    lda_controller.start()





    myWin.initalface('acc')
    myWin.initalface('turn')
    myWin.initalface('swerve')
    myWin.initalface('brake')
    myWin.setBar(2,'acc')
    # myWin.setBar(2,'brake')
    # myWin.setBar(1,'turn')
    # myWin.setBar(0,'swerve')
    myWin.setFeedBack(0,'acc')


    sys.exit(app.exec_())

