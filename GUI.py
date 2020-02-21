# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from pyqtgraph import PlotWidget
import pyqtgraph as pg
from PyQt5.QtCore import QThread

class Ui_MainWindow(object):
    def __init__(self):

        self._coin_gold0 = QtGui.QPixmap('icons/events/coin_gold0.png')
        self._coin_gold1 = QtGui.QPixmap('icons/events/coin_gold1.png')
        self._coin_gold2 = QtGui.QPixmap('icons/events/coin_gold2.png')
        self._gold_coin = QtGui.QPixmap('icons/events/coin_gold0.png')
        self._grey_coin = QtGui.QPixmap('icons/events/coin_gold1.png')



        self.grey_bar = QtGui.QPixmap('icons/bars/grey_bar.png')
        self.top_bar = QtGui.QPixmap('icons/bars/top_bar.png')
        self.medium_bar = QtGui.QPixmap('icons/bars/medium_bar.png')
        self.bottom_bar = QtGui.QPixmap('icons/bars/bottom_bar.png')



        self.green_glow = pg.QtGui.QGraphicsPixmapItem(pg.QtGui.QPixmap('icons/glow/Green-Glow.png'))
        self.orange_glow = pg.QtGui.QGraphicsPixmapItem(pg.QtGui.QPixmap('icons/glow/Orange-Glow.png'))
        self.yellow_glow = pg.QtGui.QGraphicsPixmapItem(pg.QtGui.QPixmap('icons/glow/Yellow-Glow.png'))

        self.brake_icon = QtGui.QIcon('icons/events/Brake.svg')
        self.acc_icon = QtGui.QIcon('icons/events/Accelerate.svg')
        self.turn_icon = QtGui.QIcon('icons/events/Turn.svg')
        self.swerve_icon = QtGui.QIcon('icons/events/Swerve.svg')
        pass
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
        self.verticalLayout.setContentsMargins(5, 10, 5, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bar = QtWidgets.QWidget(self.centralwidget)
        self.bar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.bar.setObjectName("bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.bar)
        self.horizontalLayout.setContentsMargins(-1, 5, 11, 5)
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
        self.next_page = QtWidgets.QPushButton(self.bar)
        self.next_page.setMaximumSize(QtCore.QSize(85, 30))
        self.next_page.setObjectName("next_page")
        self.horizontalLayout.addWidget(self.next_page)
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
        # pg.setConfigOption('background', '#17191A')
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

        self.current_score = QtWidgets.QLabel(self.down)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_score.sizePolicy().hasHeightForWidth())
        self.current_score.setSizePolicy(sizePolicy)
        self.current_score.setMinimumSize(QtCore.QSize(20, 60))
        self.current_score.setMaximumSize(QtCore.QSize(300, 120))
        font = QtGui.QFont()
        font.setFamily("Brush Script Std")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.current_score.setFont(font)
        self.current_score.setAlignment(QtCore.Qt.AlignCenter)
        self.current_score.setObjectName("CurrentScore")
        self.gridLayout_down.addWidget(self.current_score, 0, 1, 1, 1)


        self.total_score = QtWidgets.QPushButton()
        self.total_score.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.total_score.setMinimumSize(QtCore.QSize(0, 0))
        self.total_score.setMaximumSize(QtCore.QSize(250, 120))
        self.total_score.setFlat(True)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setKerning(True)
        font.setBold(True)
        font.setFamily("Brush Script Std")
        self.total_score.setStyleSheet('QPushButton {background-color: #17191A; color: white;}')
        self.total_score.setFont(font)
        self.total_score.setLayoutDirection(QtCore.Qt.RightToLeft)
        # self.TotalScore.setAlignment(QtCore.Qt.AlignCenter)
        self.total_score.setObjectName("TotalScore")
        self.gridLayout_down.addWidget(self.total_score, 0, 2, 1, 1)
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

        self.turn_bar = QtWidgets.QWidget(self.up)
        self.turn_bar.setMaximumSize(QtCore.QSize(80, 220))
        self.turn_bar.setObjectName("Turn_bar")
        self.verticalLayout_turn = QtWidgets.QVBoxLayout(self.turn_bar)
        self.verticalLayout_turn.setContentsMargins(15, 0, 15, 0)
        self.verticalLayout_turn.setSpacing(0)
        self.verticalLayout_turn.setObjectName("verticalLayout_turn")
        self.turn_bar1 = QtWidgets.QLabel(self.turn_bar)
        self.turn_bar1.setText("")
        self.turn_bar1.setObjectName("turn_bar1")
        self.verticalLayout_turn.addWidget(self.turn_bar1)
        self.turn_bar2 = QtWidgets.QLabel(self.turn_bar)
        self.turn_bar2.setText("")
        self.turn_bar2.setObjectName("turn_bar2")
        self.verticalLayout_turn.addWidget(self.turn_bar2)
        self.turn_bar3 = QtWidgets.QLabel(self.turn_bar)
        self.turn_bar3.setText("")
        self.turn_bar3.setObjectName("turn_bar3")
        self.verticalLayout_turn.addWidget(self.turn_bar3)
        self.gridLayout_up.addWidget(self.turn_bar, 0, 5, 1, 1)

        self.turn_level = QtWidgets.QWidget(self.up)
        self.turn_level.setMaximumSize(QtCore.QSize(80, 35))
        self.turn_level.setObjectName("Turn_level")
        self.gridLayout_up.addWidget(self.turn_level, 1, 5, 1, 1)

        self.acc_bar = QtWidgets.QWidget(self.up)
        self.acc_bar.setMaximumSize(QtCore.QSize(80, 220))
        self.acc_bar.setObjectName("Acc_bar")
        self.verticalLayout_acc = QtWidgets.QVBoxLayout(self.acc_bar)
        self.verticalLayout_acc.setContentsMargins(15, 0, 15, 0)
        self.verticalLayout_acc.setSpacing(0)
        self.verticalLayout_acc.setObjectName("verticalLayout_acc")
        self.acc_bar1 = QtWidgets.QLabel(self.acc_bar)
        self.acc_bar1.setText("")
        self.acc_bar1.setObjectName("acc_bar1")
        self.verticalLayout_acc.addWidget(self.acc_bar1)
        self.acc_bar2 = QtWidgets.QLabel(self.acc_bar)
        self.acc_bar2.setText("")
        self.acc_bar2.setObjectName("acc_bar2")
        self.verticalLayout_acc.addWidget(self.acc_bar2)
        self.acc_bar3 = QtWidgets.QLabel(self.acc_bar)
        self.acc_bar3.setText("")
        self.acc_bar3.setObjectName("acc_bar3")
        self.verticalLayout_acc.addWidget(self.acc_bar3)
        self.gridLayout_up.addWidget(self.acc_bar, 0, 0, 1, 1)

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
        self.brake_bar = QtWidgets.QWidget(self.up)
        self.brake_bar.setMaximumSize(QtCore.QSize(80, 220))
        self.brake_bar.setObjectName("Brake_bar")
        self.verticalLayout_brake = QtWidgets.QVBoxLayout(self.brake_bar)
        self.verticalLayout_brake.setContentsMargins(15, 0, 15, 0)
        self.verticalLayout_brake.setSpacing(0)
        self.verticalLayout_brake.setObjectName("verticalLayout_brake")
        self.brake_bar1 = QtWidgets.QLabel(self.brake_bar)
        self.brake_bar1.setText("")
        self.brake_bar1.setObjectName("brake_bar1")
        self.verticalLayout_brake.addWidget(self.brake_bar1)
        self.brake_bar2 = QtWidgets.QLabel(self.brake_bar)
        self.brake_bar2.setText("")
        self.brake_bar2.setObjectName("brake_bar2")
        self.verticalLayout_brake.addWidget(self.brake_bar2)
        self.brake_bar3 = QtWidgets.QLabel(self.brake_bar)
        self.brake_bar3.setText("")
        self.brake_bar3.setObjectName("brake_bar3")
        self.verticalLayout_brake.addWidget(self.brake_bar3)
        self.gridLayout_up.addWidget(self.brake_bar, 0, 1, 1, 1)

        self.Swerve_level = QtWidgets.QWidget(self.up)
        self.Swerve_level.setMaximumSize(QtCore.QSize(80, 35))
        self.Swerve_level.setObjectName("Swerve_level")

        self.gridLayout_up.addWidget(self.Swerve_level, 1, 6, 1, 1)
        self.Swerve_bar = QtWidgets.QWidget(self.up)
        self.Swerve_bar.setMaximumSize(QtCore.QSize(80, 220))
        self.Swerve_bar.setObjectName("Swerve_bar")
        self.verticalLayout_swerve = QtWidgets.QVBoxLayout(self.Swerve_bar)
        self.verticalLayout_swerve.setContentsMargins(15, 0, 15, 0)
        self.verticalLayout_swerve.setSpacing(0)
        self.verticalLayout_swerve.setObjectName("verticalLayout_swerve")
        self.swerve_bar1 = QtWidgets.QLabel(self.Swerve_bar)
        self.swerve_bar1.setText("")
        self.swerve_bar1.setObjectName("swerve_bar1")
        self.verticalLayout_swerve.addWidget(self.swerve_bar1)
        self.swerve_bar2 = QtWidgets.QLabel(self.Swerve_bar)
        self.swerve_bar2.setText("")
        self.swerve_bar2.setObjectName("swerve_bar2")
        self.verticalLayout_swerve.addWidget(self.swerve_bar2)
        self.swerve_bar3 = QtWidgets.QLabel(self.Swerve_bar)
        self.swerve_bar3.setText("")
        self.swerve_bar3.setObjectName("swerve_bar3")
        self.verticalLayout_swerve.addWidget(self.swerve_bar3)
        self.gridLayout_up.addWidget(self.Swerve_bar, 0, 6, 1, 1)




        self.acc_level = PlotWidget(self.up)
        self.acc_level.setMaximumSize(QtCore.QSize(80, 35))
        self.acc_level.setObjectName("Acc_level")
        self.acc_level.setFocusPolicy(QtCore.Qt.TabFocus)
        self.acc_level.getPlotItem().hideAxis('bottom')
        self.acc_level.getPlotItem().hideAxis('left')

        self.gridLayout_up.addWidget(self.acc_level, 1, 0, 1, 1)
        self.brake_level = QtWidgets.QWidget(self.up)
        self.brake_level.setMaximumSize(QtCore.QSize(80, 35))
        self.brake_level.setObjectName("Brake_level")
        self.gridLayout_up.addWidget(self.brake_level, 1, 1, 1, 1)
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
        self.next_page.setFixedSize(80,20)
        # self.visit.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        # self.mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        # beautify window
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # hide the boarder
        self.setWindowOpacity(0.98)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # set transparent window
        self.exit.clicked.connect(self.close)       # close window
        self.mini.clicked.connect(self.showMinimized)  # minimum window
        self.windowMoved.connect(self.move)  # move window


        self.acc_pic_coin = QtWidgets.QLabel(self.acc_level)
        self.acc_pic_coin.setMargin(5)
        self.acc_pic_coin.setPixmap(self._gold_coin)
        self.acc_pic_coin.setScaledContents(True)
        self.acc_pic_coin.setMaximumSize(QtCore.QSize(80, 31))

        self.brake_pic_coin = QtWidgets.QLabel(self.brake_level)
        self.brake_pic_coin.setMargin(5)
        self.brake_pic_coin.setPixmap(self._grey_coin)
        self.brake_pic_coin.setScaledContents(True)
        self.brake_pic_coin.setMaximumSize(QtCore.QSize(80, 31))


        self.turn_pic_coin = QtWidgets.QLabel(self.turn_level)
        self.turn_pic_coin.setMargin(5)
        self.turn_pic_coin.setPixmap(self._grey_coin)
        self.turn_pic_coin.setScaledContents(True)
        self.turn_pic_coin.setMaximumSize(QtCore.QSize(80, 31))


        self.swerve_pic_coin = QtWidgets.QLabel(self.Swerve_level)
        self.swerve_pic_coin.setMargin(5)
        self.swerve_pic_coin.setPixmap(self._gold_coin)
        self.swerve_pic_coin.setScaledContents(True)
        self.swerve_pic_coin.setMaximumSize(QtCore.QSize(80, 31))

        # # self.acc_bar_top = QtWidgets.QLabel(self.acc_bar1)
        # self.acc_bar1.setPixmap(self.acc_bar1)
        # self.acc_bar1.setScaledContents(True)
        # self.acc_bar1.setMaximumSize(QtCore.QSize(50, 67))
        #
        #
        # self.acc_bar2 = QtWidgets.QLabel(self.acc_bar2)
        # self.acc_bar2.setPixmap(self.acc_bar2)
        # self.acc_bar2.setScaledContents(True)
        # self.acc_bar2.setMaximumSize(QtCore.QSize(50, 67))
        #
        #
        # self.acc_bar3 = QtWidgets.QLabel(self.acc_bar3)
        # self.acc_bar3.setPixmap(self.acc_bar3)
        # self.acc_bar3.setScaledContents(True)
        # self.acc_bar3.setMaximumSize(QtCore.QSize(50, 67))


        # draw graph of lines--should be deleted later

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
        self.current_score.setText(str(score))

    # set Total score for trip
    def setTotalScore(self, score):
        self.total_score.setText(str(score) + ' points')

    def setFeedBack(self, level: int, type: str):
        if level == 0:
            self.backCircle.clear()
            self.backCircle.addItem(self.green_glow)
        elif level == 1:
            self.backCircle.clear()
            self.backCircle.addItem(self.yellow_glow)
        elif level == 2:
            self.backCircle.clear()
            self.backCircle.addItem(self.orange_glow)

        if type == 'acc':
            self.feedback.setIcon(self.acc_icon)
            self.feedback.setIconSize(QtCore.QSize(150, 150))
        elif type == 'brake':
            self.feedback.setIcon(self.brake_icon)
            self.feedback.setIconSize(QtCore.QSize(150, 150))
        elif type == 'turn':
            self.feedback.setIcon(self.turn_icon)
            self.feedback.setIconSize(QtCore.QSize(150, 150))
        elif type == 'swerve':
            self.feedback.setIcon(self.swerve_icon)
            self.feedback.setIconSize(QtCore.QSize(150, 150))




    def change_icons(self,level:int, type:str):
        if type == 'acc':
            self.change_acc_icon(level)
        elif type == 'brake':
            self.change_brake_icon(level)
        elif type == 'turn':
            self.change_turn_icon(level)
        elif type == 'swerve':
            self.change_swerve_icon(level)

    def change_acc_icon(self, level: int):
        if level == 0:
            self.acc_pic_coin.setPixmap(self._coin_gold0)
        elif level == 1:
            self.acc_pic_coin.setPixmap(self._coin_gold1)
        elif level == 2:
            self.acc_pic_coin.setPixmap(self._coin_gold2)

    def change_brake_icon(self, level: int):
        if level == 0:
            self.brake_pic_coin.setPixmap(self._coin_gold0)
        elif level == 1:
            self.brake_pic_coin.setPixmap(self._coin_gold1)
        elif level == 2:
            self.brake_pic_coin.setPixmap(self._coin_gold2)

    def change_turn_icon(self, level: int):
        if level == 0:
            self.turn_pic_coin.setPixmap(self._coin_gold0)
        elif level == 1:
            self.turn_pic_coin.setPixmap(self._coin_gold1)
        elif level == 2:
            self.turn_pic_coin.setPixmap(self._coin_gold2)

    def change_swerve_icon(self, level: int):
        if level == 0:
            self.swerve_pic_coin.setPixmap(self._coin_gold0)
        elif level == 1:
            self.swerve_pic_coin.setPixmap(self._coin_gold1)
        elif level == 2:
            self.swerve_pic_coin.setPixmap(self._coin_gold2)
    def setBar(self,level:str,type:str):
        if type == 'acc':
            self.change_acc_bar(level)
        elif type == 'brake':
            self.change_brake_bar(level)
        elif type == 'turn':
            self.change_turn_bar(level)
        elif type == 'swerve':
            self.change_swerve_bar(level)
          
    def change_acc_bar(self,level):
        if level=='safe':
            self.acc_bar1.setPixmap(self.grey_bar)
            self.acc_bar2.setPixmap(self.grey_bar)
            self.acc_bar3.setPixmap(self.bottom_bar)
        elif level=='mediumrisk':
            self.acc_bar1.setPixmap(self.grey_bar)
            self.acc_bar2.setPixmap(self.medium_bar)
            self.acc_bar3.setPixmap(self.bottom_bar)
        elif level=='highrisk':
            self.acc_bar1.setPixmap(self.top_bar)
            self.acc_bar2.setPixmap(self.medium_bar)
            self.acc_bar3.setPixmap(self.bottom_bar)
        self.acc_bar1.setScaledContents(True)
        self.acc_bar2.setScaledContents(True)
        self.acc_bar3.setScaledContents(True)
        self.acc_bar1.setMaximumSize(QtCore.QSize(50, 67))
        self.acc_bar2.setMaximumSize(QtCore.QSize(50, 67))
        self.acc_bar3.setMaximumSize(QtCore.QSize(50, 67))


    def change_turn_bar(self,level):
        if level == 'safe':
            self.turn_bar1.setPixmap(self.grey_bar)
            self.turn_bar2.setPixmap(self.grey_bar)
            self.turn_bar3.setPixmap(self.bottom_bar)
        elif level == 'mediumrisk':
            self.turn_bar1.setPixmap(self.grey_bar)
            self.turn_bar2.setPixmap(self.medium_bar)
            self.turn_bar3.setPixmap(self.bottom_bar)
        elif level == 'highrisk':
            self.turn_bar1.setPixmap(self.top_bar)
            self.turn_bar2.setPixmap(self.medium_bar)
            self.turn_bar3.setPixmap(self.bottom_bar)
        self.turn_bar1.setScaledContents(True)
        self.turn_bar2.setScaledContents(True)
        self.turn_bar3.setScaledContents(True)
        self.turn_bar1.setMaximumSize(QtCore.QSize(50, 67))
        self.turn_bar2.setMaximumSize(QtCore.QSize(50, 67))
        self.turn_bar3.setMaximumSize(QtCore.QSize(50, 67))

    def change_swerve_bar(self,level):
        if level == 'safe':
            self.swerve_bar1.setPixmap(self.grey_bar)
            self.swerve_bar2.setPixmap(self.grey_bar)
            self.swerve_bar3.setPixmap(self.bottom_bar)
        elif level == 'mediumrisk':
            self.swerve_bar1.setPixmap(self.grey_bar)
            self.swerve_bar2.setPixmap(self.medium_bar)
            self.swerve_bar3.setPixmap(self.bottom_bar)
        elif level == 'highrisk':
            self.swerve_bar1.setPixmap(self.top_bar)
            self.swerve_bar2.setPixmap(self.medium_bar)
            self.swerve_bar3.setPixmap(self.bottom_bar)
        self.swerve_bar1.setScaledContents(True)
        self.swerve_bar2.setScaledContents(True)
        self.swerve_bar3.setScaledContents(True)
        self.swerve_bar1.setMaximumSize(QtCore.QSize(50, 67))
        self.swerve_bar2.setMaximumSize(QtCore.QSize(50, 67))
        self.swerve_bar3.setMaximumSize(QtCore.QSize(50, 67))

    def change_brake_bar(self,level,):
        if level == 'safe':
            self.brake_bar1.setPixmap(self.grey_bar)
            self.brake_bar2.setPixmap(self.grey_bar)
            self.brake_bar3.setPixmap(self.bottom_bar)
        elif level == 'mediumrisk':
            self.brake_bar1.setPixmap(self.grey_bar)
            self.brake_bar2.setPixmap(self.medium_bar)
            self.brake_bar3.setPixmap(self.bottom_bar)
        elif level == 'highrisk':
            self.brake_bar1.setPixmap(self.top_bar)
            self.brake_bar2.setPixmap(self.medium_bar)
            self.brake_bar3.setPixmap(self.bottom_bar)
        self.brake_bar1.setScaledContents(True)
        self.brake_bar2.setScaledContents(True)
        self.brake_bar3.setScaledContents(True)
        self.brake_bar1.setMaximumSize(QtCore.QSize(50, 67))
        self.brake_bar2.setMaximumSize(QtCore.QSize(50, 67))
        self.brake_bar3.setMaximumSize(QtCore.QSize(50, 67))





    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.current_score.setText(_translate("MainWindow", "86"))
        self.total_score.setText(_translate("MainWindow", "1240 points"))
        self.next_page.setText(_translate("MainWindow", "Next Page>>"))


