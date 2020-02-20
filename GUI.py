# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np

class Ui_MainWindow(object):

    windowMoved = QtCore.pyqtSignal(QtCore.QPoint)

    def update2(self):
        data3 = self.data3
        ptr3 = self.ptr3
        data3[ptr3] = np.random.normal()

        ptr3 += 1
        if ptr3 >= data3.shape[0]:
            tmp = data3
            data3 = np.empty(data3.shape[0] * 2)
            data3[:tmp.shape[0]] = tmp
        self.pen1.setData(data3[:ptr3])
        self.data3 = data3
        if(ptr3>100):
            self.pen1.setPen(pg.mkPen('r', width=3))
        self.pen1.setPos(-ptr3, 0)
        self.ptr3 = ptr3

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 500)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bar = QtWidgets.QWidget(self.centralwidget)
        self.bar.setMaximumSize(QtCore.QSize(16777215, 25))
        self.bar.setObjectName("bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.bar)
        self.horizontalLayout.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exit = QtWidgets.QPushButton(self.bar)
        self.exit.setMaximumSize(QtCore.QSize(30, 20))
        self.exit.setText("")
        self.exit.setObjectName("close")
        self.horizontalLayout.addWidget(self.exit)
        self.visit = QtWidgets.QPushButton(self.bar)
        self.visit.setMaximumSize(QtCore.QSize(30, 20))
        self.visit.setText("")
        self.visit.setObjectName("visit")
        self.horizontalLayout.addWidget(self.visit)
        self.mini = QtWidgets.QPushButton(self.bar)
        self.mini.setMaximumSize(QtCore.QSize(30, 20))
        self.mini.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.mini.setText("")
        self.mini.setAutoDefault(False)
        self.mini.setDefault(False)
        self.mini.setFlat(False)
        self.mini.setObjectName("mini")
        self.horizontalLayout.addWidget(self.mini)
        spacerItem = QtWidgets.QSpacerItem(40, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.bar)
        self.Menu = QtWidgets.QGridLayout()
        self.Menu.setObjectName("Menu")
        self.down = QtWidgets.QWidget(self.centralwidget)
        self.down.setMinimumSize(QtCore.QSize(0, 130))
        self.down.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.down.setObjectName("down")
        self.gridLayout_down = QtWidgets.QGridLayout(self.down)
        self.gridLayout_down.setHorizontalSpacing(5)
        self.gridLayout_down.setObjectName("gridLayout_down")
        pg.setConfigOption('background', '#17191A')
        self.widget = PlotWidget(self.down)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setMaximumSize(QtCore.QSize(300, 120))
        self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget.setObjectName("widget")
        self.gridLayout_down.addWidget(self.widget, 0, 0, 1, 1)
        self.CurrentScore = QtWidgets.QLabel(self.down)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CurrentScore.sizePolicy().hasHeightForWidth())
        self.CurrentScore.setSizePolicy(sizePolicy)
        self.CurrentScore.setMinimumSize(QtCore.QSize(20, 60))
        self.CurrentScore.setMaximumSize(QtCore.QSize(300, 120))
        font = QtGui.QFont()
        font.setFamily("Brush Script Std")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.CurrentScore.setFont(font)
        self.CurrentScore.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentScore.setObjectName("CurrentScore")
        self.gridLayout_down.addWidget(self.CurrentScore, 0, 1, 1, 1)
        self.TotalScore = QtWidgets.QLabel(self.down)
        self.TotalScore.setMinimumSize(QtCore.QSize(0, 0))
        self.TotalScore.setMaximumSize(QtCore.QSize(250, 120))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setKerning(True)
        self.TotalScore.setFont(font)
        self.TotalScore.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.TotalScore.setAlignment(QtCore.Qt.AlignCenter)
        self.TotalScore.setObjectName("TotalScore")
        self.gridLayout_down.addWidget(self.TotalScore, 0, 2, 1, 1)
        self.Menu.addWidget(self.down, 4, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(10)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.Menu.addWidget(self.line, 1, 0, 1, 1)
        self.up = QtWidgets.QWidget(self.centralwidget)
        self.up.setMinimumSize(QtCore.QSize(0, 0))
        self.up.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.up.setObjectName("up")
        self.gridLayout_up = QtWidgets.QGridLayout(self.up)
        self.gridLayout_up.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_up.setHorizontalSpacing(0)
        self.gridLayout_up.setVerticalSpacing(0)
        self.gridLayout_up.setSpacing(0)
        self.gridLayout_up.setObjectName("gridLayout_up")

        self.Turn_bar = QtWidgets.QWidget(self.up)
        self.Turn_bar.setMaximumSize(QtCore.QSize(80, 220))
        self.Turn_bar.setObjectName("Turn_bar")
        self.gridLayout_up.addWidget(self.Turn_bar, 0, 5, 1, 1)

        self.Turn_level = QtWidgets.QWidget(self.up)
        self.Turn_level.setMaximumSize(QtCore.QSize(80, 35))
        self.Turn_level.setObjectName("Turn_level")
        self.gridLayout_up.addWidget(self.Turn_level, 1, 5, 1, 1)

        self.Acc_bar = QtWidgets.QWidget(self.up)
        self.Acc_bar.setMaximumSize(QtCore.QSize(80, 220))
        self.Acc_bar.setObjectName("Acc_bar")
        self.verticalLayout_acc = QtWidgets.QVBoxLayout(self.Acc_bar)
        self.verticalLayout_acc.setContentsMargins(15, 0, 15, 0)
        self.verticalLayout_acc.setSpacing(0)
        self.verticalLayout_acc.setObjectName("verticalLayout_acc")
        self.acc_bar1 = QtWidgets.QLabel(self.Acc_bar)
        self.acc_bar1.setText("")
        self.acc_bar1.setObjectName("acc_bar1")
        self.verticalLayout_acc.addWidget(self.acc_bar1)
        self.acc_bar2 = QtWidgets.QLabel(self.Acc_bar)
        self.acc_bar2.setText("")
        self.acc_bar2.setObjectName("acc_bar2")
        self.verticalLayout_acc.addWidget(self.acc_bar2)
        self.acc_bar3 = QtWidgets.QLabel(self.Acc_bar)
        self.acc_bar3.setText("")
        self.acc_bar3.setObjectName("acc_bar3")
        self.verticalLayout_acc.addWidget(self.acc_bar3)
        self.gridLayout_up.addWidget(self.Acc_bar, 0, 0, 1, 1)

        spacer1 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_up.addItem(spacer1, 0, 2, 1, 1)
        pg.setConfigOption('background', '#FCFCFC')

        self.backCircle = PlotWidget(self.up)
        self.backCircle.setMinimumSize(QtCore.QSize(50, 50))
        self.backCircle.setMaximumSize(QtCore.QSize(300, 320))
        self.backCircle.setObjectName("backCircle")
        self.backCircle.getPlotItem().hideAxis('bottom')
        self.backCircle.getPlotItem().hideAxis('left')
        self.backCircleLayout = QtWidgets.QGridLayout(self.backCircle)
        self.backCircleLayout.setContentsMargins(60, 50, 60, 50)
        self.backCircleLayout.setObjectName("backCircleLayout")

        self.feedback = QtWidgets.QToolButton(self.backCircle)
        self.feedback.setEnabled(False)
        self.feedback.setMinimumSize(QtCore.QSize(50, 50))
        self.feedback.setMaximumSize(QtCore.QSize(320, 320))
        self.feedback.setFocusPolicy(QtCore.Qt.TabFocus)
        self.feedback.setText("")
        self.feedback.setObjectName("feedback")


        self.backCircleLayout.addWidget(self.feedback, 0, 0, 1, 1)
        self.gridLayout_up.addWidget(self.backCircle, 0, 3, 2, 1)
        self.Brake_bar = QtWidgets.QWidget(self.up)
        self.Brake_bar.setMaximumSize(QtCore.QSize(80, 220))
        self.Brake_bar.setObjectName("Brake_bar")
        self.gridLayout_up.addWidget(self.Brake_bar, 0, 1, 1, 1)

        self.Swerve_level = QtWidgets.QWidget(self.up)
        self.Swerve_level.setMaximumSize(QtCore.QSize(80, 35))
        self.Swerve_level.setObjectName("Swerve_level")

        self.gridLayout_up.addWidget(self.Swerve_level, 1, 6, 1, 1)
        self.Swerve_bar = QtWidgets.QWidget(self.up)
        self.Swerve_bar.setMaximumSize(QtCore.QSize(80, 220))
        self.Swerve_bar.setObjectName("Swerve_bar")
        self.gridLayout_up.addWidget(self.Swerve_bar, 0, 6, 1, 1)

        self.Acc_level = PlotWidget(self.up)
        self.Acc_level.setMaximumSize(QtCore.QSize(80, 35))
        self.Acc_level.setObjectName("Acc_level")
        self.Acc_level.setFocusPolicy(QtCore.Qt.TabFocus)
        self.Acc_level.getPlotItem().hideAxis('bottom')
        self.Acc_level.getPlotItem().hideAxis('left')

        self.gridLayout_up.addWidget(self.Acc_level, 1, 0, 1, 1)
        self.Brake_level = QtWidgets.QWidget(self.up)
        self.Brake_level.setMaximumSize(QtCore.QSize(80, 35))
        self.Brake_level.setObjectName("Brake_level")
        self.gridLayout_up.addWidget(self.Brake_level, 1, 1, 1, 1)
        spacer2 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_up.addItem(spacer2, 0, 4, 1, 1)
        self.Menu.addWidget(self.up, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.Menu)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # these are three control buttons
        self.exit.setFixedSize(15, 15)
        self.visit.setFixedSize(15, 15)
        self.mini.setFixedSize(15, 15)
        self.exit.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        # self.visit.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        # self.mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        # beautify window
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # hide the boarder
        self.setWindowOpacity(0.98)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # set transparent window
        self.exit.clicked.connect(self.close)       # close window
        self.mini.clicked.connect(self.showMinimized)  # minimum window
        self.windowMoved.connect(self.move)  # move window

        self.greenGlow = pg.QtGui.QGraphicsPixmapItem(pg.QtGui.QPixmap('icons/glow/Green-Glow.png'))
        self.orangeGlow = pg.QtGui.QGraphicsPixmapItem(pg.QtGui.QPixmap('icons/glow/Orange-Glow.png'))
        self.yellowGlow = pg.QtGui.QGraphicsPixmapItem(pg.QtGui.QPixmap('icons/glow/Yellow-Glow.png'))

        self.brakeIcon = QtGui.QIcon('icons/events/Brake.svg')
        self.accIcon = QtGui.QIcon('icons/events/Accelerate.svg')
        self.turnIcon = QtGui.QIcon('icons/events/Turn.svg')
        self.swerveIcon = QtGui.QIcon('icons/events/Swerve.svg')
        # self.feedback.setIcon(img3)
        # self.feedback.setIconSize(QtCore.QSize(120,120))


        gold_coin = QtGui.QPixmap('icons/events/coin_gold0.png')
        grey_coin = QtGui.QPixmap('icons/events/coin_gold1.png')
        acc_pic_coin = QtWidgets.QLabel(self.Acc_level)
        acc_pic_coin.setMargin(5)
        acc_pic_coin.setPixmap(gold_coin)
        acc_pic_coin.setScaledContents(True)
        acc_pic_coin.setMaximumSize(QtCore.QSize(80, 31))

        brake_pic_coin = QtWidgets.QLabel(self.Brake_level)
        brake_pic_coin.setMargin(5)
        brake_pic_coin.setPixmap(grey_coin)
        brake_pic_coin.setScaledContents(True)
        brake_pic_coin.setMaximumSize(QtCore.QSize(80, 31))

        turn_pic_coin = QtWidgets.QLabel(self.Turn_level)
        turn_pic_coin.setMargin(5)
        turn_pic_coin.setPixmap(grey_coin)
        turn_pic_coin.setScaledContents(True)
        turn_pic_coin.setMaximumSize(QtCore.QSize(80, 31))

        swerve_pic_coin = QtWidgets.QLabel(self.Swerve_level)
        swerve_pic_coin.setMargin(5)
        swerve_pic_coin.setPixmap(gold_coin)
        swerve_pic_coin.setScaledContents(True)
        swerve_pic_coin.setMaximumSize(QtCore.QSize(80, 31))

        self.grey_bar = QtGui.QPixmap('icons/bars/grey_bar.png')
        self.top_bar = QtGui.QPixmap('icons/bars/top_bar.png')
        self.medium_bar = QtGui.QPixmap('icons/bars/medium_bar.png')
        self.bottom_bar = QtGui.QPixmap('icons/bars/bottom_bar.png')
        acc_bar_top = QtWidgets.QLabel(self.acc_bar1)
        acc_bar_top.setPixmap(self.top_bar)
        acc_bar_top.setScaledContents(True)
        acc_bar_top.setMaximumSize(QtCore.QSize(50, 67))

        acc_bar_medium = QtWidgets.QLabel(self.acc_bar2)
        acc_bar_medium.setPixmap(self.medium_bar)
        acc_bar_medium.setScaledContents(True)
        acc_bar_medium.setMaximumSize(QtCore.QSize(50, 67))

        acc_bar_bottom = QtWidgets.QLabel(self.acc_bar3)
        acc_bar_bottom.setPixmap(self.bottom_bar)
        acc_bar_bottom.setScaledContents(True)
        acc_bar_bottom.setMaximumSize(QtCore.QSize(50, 67))

        # draw graph of lines

        self.widget.setDownsampling(mode='peak')
        self.widget.setClipToView(True)
        self.widget.setXRange(0, 100)
        self.widget.setLimits(xMax=0)
        self.pen1 = self.widget.plot()
        self.pen1.setPen(pg.mkPen('y', width=3))
        self.data3 = np.empty(10)
        self.ptr3 = 0


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def mousePressEvent(self,event):
        if event.button() == QtCore.Qt.LeftButton:
            self.mPos = event.pos()
        event.accept()

    def mouseReleaseEvent(self, event):
        self.mPos = None
        event.accept()

    def mouseMoveEvent(self,event):
        if event.buttons() == QtCore.Qt.LeftButton and self.mPos:
            self.windowMoved.emit(self.mapToGlobal(event.pos() - self.mPos))
        event.accept()

    # set current score and update
    def setCurrentScore(self, score):
        self.CurrentScore.setText(str(score))

    # set Total score for trip
    def setTotalScore(self, score):
        self.TotalScore.setText(str(score)+' points')

    def setFeedBack(self, level, type):
        if level == 0:
            self.backCircle.clear()
            self.backCircle.addItem(self.greenGlow)
        elif level == 1:
            self.backCircle.clear()
            self.backCircle.addItem(self.yellowGlow)
        elif level == 2:
            self.backCircle.clear()
            self.backCircle.addItem(self.orangeGlow)

        if type == 'acc':
            self.feedback.setIcon(self.accIcon)
            self.feedback.setIconSize(QtCore.QSize(150, 150))
        elif type == 'brake':
            self.feedback.setIcon(self.brakeIcon)
            self.feedback.setIconSize(QtCore.QSize(150, 150))
        elif type == 'turn':
            self.feedback.setIcon(self.turnIcon)
            self.feedback.setIconSize(QtCore.QSize(150, 150))
        elif type == 'swerve':
            self.feedback.setIcon(self.swerveIcon)
            self.feedback.setIconSize(QtCore.QSize(150, 150))




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CurrentScore.setText(_translate("MainWindow", "86"))
        self.TotalScore.setText(_translate("MainWindow", "1240 points"))
        self.feedback.setText(_translate("MainWindow", "..."))
from pyqtgraph import PlotWidget
import pyqtgraph as pg
