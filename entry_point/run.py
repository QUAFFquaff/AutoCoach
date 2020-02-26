from ctypes import c_bool
from entry_point.DetectProcess2 import *
from entry_point.DetectProcess import *
from entry_point.Event import *






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
        self.processLock = args[1]
        self.SVM_flag = args[2]

    def run(self):
        i = 0
        while True:
            print(self.SVM_flag.value)

            i +=1
            if not self.eventQueue.empty():
                score = self.eventQueue.get()

                self.back_signal.emit(score)





def run():
    eventQueue = multiprocessing.Queue()
    processLock = multiprocessing.Lock()
    speed = multiprocessing.Value("i", 0)
    SVM_flag = multiprocessing.Value("i", 0)
    LDA_flag = multiprocessing.Value(c_bool, True)

    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()




    timer = pg.QtCore.QTimer()
    timer.timeout.connect(myWin.update2)
    timer.start(50)

    eventDetectP = DetectProcess2(eventQueue, processLock, speed, SVM_flag)
    eventDetectP.daemon = True
    eventDetectP.start()

    listener = ListenerThread(args=(eventQueue, processLock, SVM_flag))
    listener.back_signal.connect(myWin.setCurrentScore)
    listener.start()

    myWin.setCurrentScore(45)
    myWin.setFeedBack(1,'acc')


    myWin.setBar('safe','acc')
    myWin.setBar('mediumrisk','brake')
    myWin.setBar('highrisk','turn')
    myWin.setBar('safe','swerve')


    sys.exit(app.exec_())

