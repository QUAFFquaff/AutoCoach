from ctypes import c_bool
from entry_point.DetectProcess2 import *
from entry_point.DetectProcess import *
from entry_point.Event import *
from entry_point.Listener import ListenerThread
import joblib






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




def run():
    eventQueue = multiprocessing.Queue()
    processLock = multiprocessing.Lock()
    speed = multiprocessing.Value("i", 0)
    SVM_flag = multiprocessing.Value("i", 0)
    LDA_flag = multiprocessing.Value(c_bool, True)

    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()




    # timer = pg.QtCore.QTimer()
    # timer.timeout.connect(myWin.update_flowing_score)
    # timer.start(50)

    eventDetectP = DetectProcess2(eventQueue, processLock, speed, SVM_flag, LDA_flag)
    eventDetectP.daemon = True
    eventDetectP.start()

    # listener = ListenerThread(eventQueue, processLock, speed, SVM_flag, LDA_flag)
    # listener.back_signal.connect(myWin.setCurrentScore)
    # listener.start()

    myWin.setCurrentScore(45)
    myWin.setFeedBack(1,'acc')


    myWin.setBar('safe','acc')
    myWin.setBar('mediumrisk','brake')
    myWin.setBar('highrisk','turn')
    myWin.setBar('safe','swerve')


    sys.exit(app.exec_())

