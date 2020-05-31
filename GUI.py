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



        self.grey_bar = QtGui.QPixmap('icons/bars/grey_wide.png')
        self.top_bar = QtGui.QPixmap('icons/bars/red_wide.png')
        self.medium_bar = QtGui.QPixmap('icons/bars/yellow_wide.png')
        self.bottom_bar = QtGui.QPixmap('icons/bars/green_wide.png')



        self.green_glow = pg.QtGui.QGraphicsPixmapItem(pg.QtGui.QPixmap('icons/glow/Orange-Glow.png'))
        self.orange_glow = pg.QtGui.QGraphicsPixmapItem(pg.QtGui.QPixmap('icons/glow/Orange-Glow.png'))
        self.yellow_glow = pg.QtGui.QGraphicsPixmapItem(pg.QtGui.QPixmap('icons/glow/Yellow-Glow.png'))

        self.acc_icon_png = QtGui.QPixmap('icons/bars/acc_icon_g.png')
        self.brake_icon_png = QtGui.QPixmap('icons/bars/brake_icon_g.png')
        self.turn_icon_png = QtGui.QPixmap('icons/bars/turn_icon_g.png')
        self.swerve_icon_png = QtGui.QPixmap('icons/bars/swerve_icon_g.png')
        pass
    windowMoved = QtCore.pyqtSignal(QtCore.QPoint)

    def update_flowing_score(self):
        data3 = self.data3
        ptr3 = self.ptr3
        data3[ptr3] = np.random.normal()

        ptr3 += 1
        if ptr3 >= data3.shape[0]:
            tmp = data3
            data3 = np.empty(data3.shape[0] * 2)
            data3[:tmp.shape[0]] = tmp
        self.pen_y.setData(data3[:ptr3])
        self.data3 = data3
        if(data3[ptr3]>100):
            self.pen_y.setPen(pg.mkPen('r', width=3))
        if(data3[ptr3]<100):
            self.pen_y.setPen(pg.mkPen('y', width=3))
        self.pen_y.setPos(-ptr3, 0)
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
        self.down.setMaximumSize(QtCore.QSize(16777215, 130))
        self.down.setObjectName("down")
        self.down.setStyleSheet('QWidget {background-color: #000000; color: yellow;}')
        self.gridLayout_down = QtWidgets.QGridLayout(self.down)
        self.gridLayout_down.setHorizontalSpacing(5)
        self.gridLayout_down.setObjectName("gridLayout_down")
        # pg.setConfigOption('background', '#17191A')
        self.flowing_scores = PlotWidget(self.down)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flowing_scores.sizePolicy().hasHeightForWidth())
        self.flowing_scores.setSizePolicy(sizePolicy)
        self.flowing_scores.setMinimumSize(QtCore.QSize(0, 0))
        self.flowing_scores.setMaximumSize(QtCore.QSize(300, 120))
        self.flowing_scores.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.flowing_scores.setObjectName("widget")
        self.gridLayout_down.addWidget(self.flowing_scores, 0, 0, 1, 1)

        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.total_coins_img = QtWidgets.QLabel(self.down)
        self.total_coins_img.setMinimumSize(QtCore.QSize(100, 0))
        self.total_coins_img.setObjectName("total_coins_img")
        self.horizontalLayout_2.addWidget(self.total_coins_img)
        self.label_2 = QtWidgets.QLabel(self.down)
        self.label_2.setMinimumSize(QtCore.QSize(60, 40))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.total_coins_score = QtWidgets.QLabel(self.down)
        self.total_coins_score.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.total_coins_score.setFont(font)
        self.total_coins_score.setObjectName("total_coins_score")
        self.horizontalLayout_2.addWidget(self.total_coins_score)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.total_coins = QtWidgets.QLabel(self.down)
        self.total_coins.setMinimumSize(QtCore.QSize(0, 10))
        self.total_coins.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.total_coins.setFont(font)
        self.total_coins.setAlignment(QtCore.Qt.AlignCenter)
        self.total_coins.setObjectName("total_coins")
        self.verticalLayout_4.addWidget(self.total_coins)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.trip_score_img = QtWidgets.QLabel(self.down)
        self.trip_score_img.setMinimumSize(QtCore.QSize(100, 0))
        self.trip_score_img.setObjectName("trip_score_img")
        self.horizontalLayout_3.addWidget(self.trip_score_img)
        self.label_3 = QtWidgets.QLabel(self.down)
        self.label_3.setMinimumSize(QtCore.QSize(60, 0))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.trip_score_score = QtWidgets.QLabel(self.down)
        self.trip_score_score.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.trip_score_score.setFont(font)
        self.trip_score_score.setObjectName("trip_score_score")
        self.horizontalLayout_3.addWidget(self.trip_score_score)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.trip_score = QtWidgets.QLabel(self.down)
        self.trip_score.setMinimumSize(QtCore.QSize(0, 9))
        self.trip_score.setMaximumSize(QtCore.QSize(250, 10))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        font.setKerning(True)
        self.trip_score.setFont(font)
        self.trip_score.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.trip_score.setAlignment(QtCore.Qt.AlignCenter)
        self.trip_score.setObjectName("trip_score")
        self.verticalLayout_4.addWidget(self.trip_score)
        self.gridLayout_down.addLayout(self.verticalLayout_4, 0, 4, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.current_score = QtWidgets.QLabel(self.down)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_score.sizePolicy().hasHeightForWidth())
        self.current_score.setSizePolicy(sizePolicy)
        self.current_score.setMinimumSize(QtCore.QSize(200, 60))
        self.current_score.setMaximumSize(QtCore.QSize(250, 60))
        font = QtGui.QFont()
        font.setFamily("Brush Script Std")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.current_score.setFont(font)
        self.current_score.setAlignment(QtCore.Qt.AlignCenter)
        self.current_score.setObjectName("CurrentScore")
        self.verticalLayout_3.addWidget(self.current_score)
        self.current_score_text = QtWidgets.QLabel(self.down)
        self.current_score_text.setMaximumSize(QtCore.QSize(250, 16777215))
        self.current_score_text.setMinimumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(15)
        self.current_score_text.setFont(font)
        self.current_score_text.setAlignment(QtCore.Qt.AlignCenter)
        self.current_score_text.setObjectName("label")
        self.verticalLayout_3.addWidget(self.current_score_text)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.gridLayout_down.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        # font = QtGui.QFont()
        # font.setPointSize(15)
        # font.setKerning(True)
        # font.setBold(True)
        # font.setFamily("Brush Script Std")
        self.Menu.addWidget(self.down, 4, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(10)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.Menu.addWidget(self.line, 1, 0, 1, 1)
        self.up = QtWidgets.QWidget(self.centralwidget)
        self.up.setMinimumSize(QtCore.QSize(0, 320))
        self.up.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.up.setObjectName("up")

        self.up.setStyleSheet('QWidget {background-color: #000000; color: blue;}')
        self.gridLayout_up = QtWidgets.QGridLayout(self.up)
        self.gridLayout_up.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_up.setHorizontalSpacing(0)
        self.gridLayout_up.setVerticalSpacing(20)
        self.gridLayout_up.setObjectName("gridLayout_up")

        self.brake_bar = QtWidgets.QWidget(self.up)
        self.brake_bar.setMinimumSize(QtCore.QSize(80, 220))
        self.brake_bar.setMaximumSize(QtCore.QSize(80, 250))
        self.brake_bar.setObjectName("brake_bar")
        self.verticalLayout_break = QtWidgets.QVBoxLayout(self.brake_bar)
        self.verticalLayout_break.setContentsMargins(15, 0, 15, 0)
        self.verticalLayout_break.setSpacing(0)
        self.verticalLayout_break.setObjectName("verticalLayout_break")
        self.brake_icon = QtWidgets.QLabel(self.brake_bar)
        self.brake_icon.setMinimumSize(QtCore.QSize(40, 40))
        self.brake_icon.setMaximumSize(QtCore.QSize(40, 40))
        self.brake_icon.setText("")
        self.brake_icon.setObjectName("brake_icon")
        self.verticalLayout_break.addWidget(self.brake_icon)
        self.brake_bar1 = QtWidgets.QLabel(self.brake_bar)
        self.brake_bar1.setText("")
        self.brake_bar1.setObjectName("brake_bar1")
        self.verticalLayout_break.addWidget(self.brake_bar1)
        self.brake_bar2 = QtWidgets.QLabel(self.brake_bar)
        self.brake_bar2.setText("")
        self.brake_bar2.setObjectName("brake_bar2")
        self.verticalLayout_break.addWidget(self.brake_bar2)
        self.brake_bar3 = QtWidgets.QLabel(self.brake_bar)
        self.brake_bar3.setText("")
        self.brake_bar3.setObjectName("brake_bar3")
        self.verticalLayout_break.addWidget(self.brake_bar3)
        self.brake_bar4 = QtWidgets.QLabel(self.brake_bar)
        self.brake_bar4.setObjectName("brake_bar4")
        self.verticalLayout_break.addWidget(self.brake_bar4)
        self.brake_bar5 = QtWidgets.QLabel(self.brake_bar)
        self.brake_bar5.setObjectName("label_4")
        self.verticalLayout_break.addWidget(self.brake_bar5)
        self.gridLayout_up.addWidget(self.brake_bar, 1, 1, 2, 1)
        self.acc_bar = QtWidgets.QWidget(self.up)
        self.acc_bar.setMinimumSize(QtCore.QSize(80, 220))
        self.acc_bar.setMaximumSize(QtCore.QSize(80, 250))
        self.acc_bar.setObjectName("acc_bar")
        self.verticalLayout_acc = QtWidgets.QVBoxLayout(self.acc_bar)
        self.verticalLayout_acc.setContentsMargins(15, 0, 15, 0)
        self.verticalLayout_acc.setSpacing(0)
        self.verticalLayout_acc.setObjectName("verticalLayout_acc")
        self.acc_icon = QtWidgets.QLabel(self.acc_bar)
        self.acc_icon.setMinimumSize(QtCore.QSize(40, 40))
        self.acc_icon.setMaximumSize(QtCore.QSize(40, 40))
        # self.acc_icon.setLayoutDirection(QtCore.Qt.LeftToRight)
        # self.acc_icon.setAutoFillBackground(False)
        # self.acc_icon.setFrameShape(QtWidgets.QFrame.NoFrame)
        # self.acc_icon.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.acc_icon.setText("")
        self.acc_icon.setObjectName("acc_icon")
        self.verticalLayout_acc.addWidget(self.acc_icon)
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
        self.acc_bar4 = QtWidgets.QLabel(self.acc_bar)
        self.acc_bar4.setObjectName("accbar4")
        self.verticalLayout_acc.addWidget(self.acc_bar4)
        self.acc_bar5 = QtWidgets.QLabel(self.acc_bar)
        self.acc_bar5.setObjectName("acc_bar5")
        self.verticalLayout_acc.addWidget(self.acc_bar5)
        self.gridLayout_up.addWidget(self.acc_bar, 1, 0, 2, 1)
        self.turn_bar = QtWidgets.QWidget(self.up)
        self.turn_bar.setMinimumSize(QtCore.QSize(80, 220))
        self.turn_bar.setMaximumSize(QtCore.QSize(80, 250))
        self.turn_bar.setObjectName("turn_bar")
        self.verticalLayout_turn = QtWidgets.QVBoxLayout(self.turn_bar)
        self.verticalLayout_turn.setContentsMargins(15, 0, 15, 0)
        self.verticalLayout_turn.setSpacing(0)
        self.verticalLayout_turn.setObjectName("verticalLayout_turn")
        self.turn_icon = QtWidgets.QLabel(self.turn_bar)
        self.turn_icon.setMinimumSize(QtCore.QSize(40, 40))
        self.turn_icon.setMaximumSize(QtCore.QSize(40, 40))
        self.turn_icon.setText("")
        self.turn_icon.setObjectName("turn_icon")
        self.verticalLayout_turn.addWidget(self.turn_icon)
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
        self.turn_bar4 = QtWidgets.QLabel(self.turn_bar)
        self.turn_bar4.setObjectName("turn_bar4")
        self.verticalLayout_turn.addWidget(self.turn_bar4)
        self.turn_bar5 = QtWidgets.QLabel(self.turn_bar)
        self.turn_bar5.setObjectName("turn_bar5")
        self.verticalLayout_turn.addWidget(self.turn_bar5)
        self.gridLayout_up.addWidget(self.turn_bar, 1, 5, 2, 1)
        self.swerve_bar = QtWidgets.QWidget(self.up)
        self.swerve_bar.setMinimumSize(QtCore.QSize(80, 220))
        self.swerve_bar.setMaximumSize(QtCore.QSize(80, 250))
        self.swerve_bar.setObjectName("swerve_bar")
        self.verticalLayout_swerve = QtWidgets.QVBoxLayout(self.swerve_bar)
        self.verticalLayout_swerve.setContentsMargins(15, 0, 15, 0)
        self.verticalLayout_swerve.setSpacing(0)
        self.verticalLayout_swerve.setObjectName("verticalLayout_swerve")
        self.swerve_icon = QtWidgets.QLabel(self.swerve_bar)
        self.swerve_icon.setMinimumSize(QtCore.QSize(40, 40))
        self.swerve_icon.setMaximumSize(QtCore.QSize(40, 40))
        self.swerve_icon.setText("")
        self.swerve_icon.setObjectName("swerve_icon")
        self.verticalLayout_swerve.addWidget(self.swerve_icon)
        self.swerve_bar1 = QtWidgets.QLabel(self.swerve_bar)
        self.swerve_bar1.setText("")
        self.swerve_bar1.setObjectName("swerve_bar1")
        self.verticalLayout_swerve.addWidget(self.swerve_bar1)
        self.swerve_bar2 = QtWidgets.QLabel(self.swerve_bar)
        self.swerve_bar2.setText("")
        self.swerve_bar2.setObjectName("swerve_bar2")
        self.verticalLayout_swerve.addWidget(self.swerve_bar2)
        self.swerve_bar3 = QtWidgets.QLabel(self.swerve_bar)
        self.swerve_bar3.setText("")
        self.swerve_bar3.setObjectName("swerve_bar3")
        self.verticalLayout_swerve.addWidget(self.swerve_bar3)
        self.swerve_bar4 = QtWidgets.QLabel(self.swerve_bar)
        self.swerve_bar4.setObjectName("swerve_bar4")
        self.verticalLayout_swerve.addWidget(self.swerve_bar4)
        self.swerve_bar5 = QtWidgets.QLabel(self.swerve_bar)
        self.swerve_bar5.setObjectName("swerve_bar5")
        self.verticalLayout_swerve.addWidget(self.swerve_bar5)
        self.gridLayout_up.addWidget(self.swerve_bar, 1, 6, 2, 1)
        self.gridLayout_up.addWidget(self.acc_bar, 1, 0, 1, 1)


        pg.setConfigOption('background', '#000000')

        self.backCircle = PlotWidget(self.up)
        # self.backCircle = QtWidgets.QWidget(self.up)
        self.backCircle.setMinimumSize(QtCore.QSize(50, 50))
        self.backCircle.setMaximumSize(QtCore.QSize(249, 249))
        self.backCircle.setObjectName("backCircle")
        self.backCircle.getPlotItem().hideAxis('bottom')
        self.backCircle.getPlotItem().hideAxis('left')
        self.backCircleLayout = QtWidgets.QGridLayout(self.backCircle)
        self.backCircleLayout.setContentsMargins(58, 50, 60, 50)
        self.backCircleLayout.setObjectName("backCircleLayout")
        # self.backCircle.setStyleSheet('QWidget {background-color: red; color: blue;}')

        self.feedback = QtWidgets.QLabel(self.backCircle)
        self.feedback.setMinimumSize(QtCore.QSize(50, 50))
        self.feedback.setMaximumSize(QtCore.QSize(320, 320))
        self.feedback.setText("")
        self.feedback.setAlignment(QtCore.Qt.AlignCenter)
        self.feedback.setObjectName("feedback")

        # self.feedback.setStyleSheet('QWidget {background-color: yellow; color: blue;}')
        self.backCircleLayout.addWidget(self.feedback, 0, 0, 1, 1)
        self.gridLayout_up.addWidget(self.backCircle, 0, 3, 2, 1)
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


        self._badge1 = QtGui.QPixmap('icons/bars/Car.png')
        self._badge2 = QtGui.QPixmap('icons/events/Less_Coins.png')
        # self._badge3 = QtGui.QPixmap('icons/Badges/png/003-bronze-medal.png')

        self.label_3.setPixmap(self._badge1)
        self.label_3.setScaledContents(True)
        self.label_3.setMaximumSize(QtCore.QSize(10, 40))

        self.label_2.setPixmap(self._badge2)
        self.label_2.setScaledContents(True)
        self.label_2.setMaximumSize(QtCore.QSize(20,30))

        self.total_coins_score.setStyleSheet('QWidget {background-color: #000000; color: yellow;}')
        self.total_coins.setStyleSheet('QWidget {background-color: #000000; color: gray;}')
        self.trip_score_score.setStyleSheet('QWidget {background-color: #000000; color: yellow;}')
        self.trip_score.setStyleSheet('QWidget {background-color: #000000; color: gray;}')
        self.current_score_text.setStyleSheet('QWidget {background-color: #000000; color: gray;}')
        # beautify window
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # hide the boarder
        # self.setWindowOpacity(0.98)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # set transparent window

        self.exit.clicked.connect(self.close)       # close window
        self.mini.clicked.connect(self.showMinimized)  # minimum window
        self.windowMoved.connect(self.move)  # move window


        # draw graph of lines
        self.flowing_scores.setDownsampling(mode='peak')
        self.flowing_scores.setClipToView(True)
        self.flowing_scores.setXRange(0, 100)
        self.flowing_scores.setLimits(xMax=0)
        self.pen_y = self.flowing_scores.plot()
        self.pen_y.setPen(pg.mkPen('y', width=3))
        self.data3 = np.empty(10)
        self.ptr3 = 0

        #draw acc icon
        self.acc_icon.setPixmap(self.acc_icon_png)
        self.acc_icon.setScaledContents(True)
        self.acc_icon.setMaximumSize(QtCore.QSize(40, 40))
        self.turn_icon.setPixmap(self.turn_icon_png)
        self.turn_icon.setScaledContents(True)
        self.turn_icon.setMaximumSize(QtCore.QSize(40, 40))
        self.brake_icon.setPixmap(self.brake_icon_png)
        self.brake_icon.setScaledContents(True)
        self.brake_icon.setMaximumSize(QtCore.QSize(40, 40))
        self.swerve_icon.setPixmap(self.swerve_icon_png)
        self.swerve_icon.setScaledContents(True)
        self.swerve_icon.setMaximumSize(QtCore.QSize(40, 40))

        self.setFeedBack(0,'acc')

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
        self.current_score.setText( str(score))

    # set Total score for trip
    def setTotalScore(self, score):
        self.trip_score.setText(str(score))

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

        self.feedback.setPixmap(self.acc_icon_png)
        if type == 'acc':
            self.feedback.setPixmap(self.acc_icon_png)
            self.feedback.setScaledContents(True)
            self.feedback.setMaximumSize(QtCore.QSize(100, 150))
        elif type == 'brake':
            self.feedback.setPixmap(self.brake_icon_png)
            self.feedback.setScaledContents(True)
            self.feedback.setMaximumSize(QtCore.QSize(100, 150))
        elif type == 'turn':
            self.feedback.setPixmap(self.turn_icon_png)
            self.feedback.setScaledContents(True)
            self.feedback.setMaximumSize(QtCore.QSize(100, 150))
        elif type == 'swerve':
            self.feedback.setPixmap(self.swerve_icon_png)
            self.feedback.setScaledContents(True)
            self.feedback.setMaximumSize(QtCore.QSize(100, 150))
        else:
            self.feedback.clear()



    def setBar(self, level: int, type: str):
        if type == 'acc':
            self.initalface(type)
            self.change_acc_bar(level)
        elif type == 'brake':
            self.initalface(type)
            self.change_brake_bar(level)
        elif type == 'turn':
            self.initalface(type)
            self.change_turn_bar(level)
        elif type == 'swerve':
            self.initalface(type)
            self.change_swerve_bar(level)

    def initalface(self, type: str):
        if type == 'acc':
            self.acc_bar1.setPixmap(self.grey_bar)
            self.acc_bar2.setPixmap(self.grey_bar)
            self.acc_bar3.setPixmap(self.grey_bar)
            self.acc_bar4.setPixmap(self.grey_bar)
            self.acc_bar5.setPixmap(self.grey_bar)
            self.acc_bar1.setScaledContents(True)
            self.acc_bar2.setScaledContents(True)
            self.acc_bar3.setScaledContents(True)
            self.acc_bar4.setScaledContents(True)
            self.acc_bar5.setScaledContents(True)
            self.acc_bar1.setMaximumSize(QtCore.QSize(40, 47))
            self.acc_bar2.setMaximumSize(QtCore.QSize(40, 47))
            self.acc_bar3.setMaximumSize(QtCore.QSize(40, 47))
            self.acc_bar4.setMaximumSize(QtCore.QSize(40, 47))
            self.acc_bar5.setMaximumSize(QtCore.QSize(40, 47))

        elif type == 'turn':
            self.turn_bar1.setPixmap(self.grey_bar)
            self.turn_bar2.setPixmap(self.grey_bar)
            self.turn_bar3.setPixmap(self.grey_bar)
            self.turn_bar4.setPixmap(self.grey_bar)
            self.turn_bar5.setPixmap(self.grey_bar)
            self.turn_bar1.setScaledContents(True)
            self.turn_bar2.setScaledContents(True)
            self.turn_bar3.setScaledContents(True)
            self.turn_bar4.setScaledContents(True)
            self.turn_bar5.setScaledContents(True)
            self.turn_bar1.setMaximumSize(QtCore.QSize(40, 47))
            self.turn_bar2.setMaximumSize(QtCore.QSize(40, 47))
            self.turn_bar3.setMaximumSize(QtCore.QSize(40, 47))
            self.turn_bar4.setMaximumSize(QtCore.QSize(40, 47))
            self.turn_bar5.setMaximumSize(QtCore.QSize(40, 47))

        elif type == 'swerve':
            self.swerve_bar1.setPixmap(self.grey_bar)
            self.swerve_bar2.setPixmap(self.grey_bar)
            self.swerve_bar3.setPixmap(self.grey_bar)
            self.swerve_bar4.setPixmap(self.grey_bar)
            self.swerve_bar5.setPixmap(self.grey_bar)
            self.swerve_bar1.setScaledContents(True)
            self.swerve_bar2.setScaledContents(True)
            self.swerve_bar3.setScaledContents(True)
            self.swerve_bar4.setScaledContents(True)
            self.swerve_bar5.setScaledContents(True)
            self.swerve_bar1.setMaximumSize(QtCore.QSize(40, 47))
            self.swerve_bar2.setMaximumSize(QtCore.QSize(40, 47))
            self.swerve_bar3.setMaximumSize(QtCore.QSize(40, 47))
            self.swerve_bar4.setMaximumSize(QtCore.QSize(40, 47))
            self.swerve_bar5.setMaximumSize(QtCore.QSize(40, 47))

        elif type == 'brake':
            self.brake_bar1.setPixmap(self.grey_bar)
            self.brake_bar2.setPixmap(self.grey_bar)
            self.brake_bar3.setPixmap(self.grey_bar)
            self.brake_bar4.setPixmap(self.grey_bar)
            self.brake_bar5.setPixmap(self.grey_bar)
            self.brake_bar1.setScaledContents(True)
            self.brake_bar2.setScaledContents(True)
            self.brake_bar3.setScaledContents(True)
            self.brake_bar4.setScaledContents(True)
            self.brake_bar5.setScaledContents(True)
            self.brake_bar1.setMaximumSize(QtCore.QSize(40, 47))
            self.brake_bar2.setMaximumSize(QtCore.QSize(40, 47))
            self.brake_bar3.setMaximumSize(QtCore.QSize(40, 47))
            self.brake_bar5.setMaximumSize(QtCore.QSize(40, 47))
            self.brake_bar4.setMaximumSize(QtCore.QSize(40, 47))

    def change_acc_bar(self, level: int):
        if level == 0:
            self.acc_bar1.setPixmap(self.grey_bar)
            self.acc_bar2.setPixmap(self.grey_bar)
            self.acc_bar3.setPixmap(self.bottom_bar)
        elif level == 1:
            self.acc_bar1.setPixmap(self.grey_bar)
            self.acc_bar2.setPixmap(self.medium_bar)
            self.acc_bar3.setPixmap(self.bottom_bar)
        elif level == 2:
            self.acc_bar1.setPixmap(self.top_bar)
            self.acc_bar2.setPixmap(self.medium_bar)
            self.acc_bar3.setPixmap(self.bottom_bar)

        self.acc_bar1.setScaledContents(True)
        self.acc_bar2.setScaledContents(True)
        self.acc_bar3.setScaledContents(True)
        self.acc_bar1.setMaximumSize(QtCore.QSize(40, 47))
        self.acc_bar2.setMaximumSize(QtCore.QSize(40, 47))
        self.acc_bar3.setMaximumSize(QtCore.QSize(40, 47))



    def change_turn_bar(self, level: int):
        if level == 0:
            self.turn_bar1.setPixmap(self.grey_bar)
            self.turn_bar2.setPixmap(self.grey_bar)
            self.turn_bar3.setPixmap(self.bottom_bar)
        elif level == 1:
            self.turn_bar1.setPixmap(self.grey_bar)
            self.turn_bar2.setPixmap(self.medium_bar)
            self.turn_bar3.setPixmap(self.bottom_bar)
        elif level == 2:
            self.turn_bar1.setPixmap(self.top_bar)
            self.turn_bar2.setPixmap(self.medium_bar)
            self.turn_bar3.setPixmap(self.bottom_bar)
        self.turn_bar1.setScaledContents(True)
        self.turn_bar2.setScaledContents(True)
        self.turn_bar3.setScaledContents(True)
        self.turn_bar1.setMaximumSize(QtCore.QSize(40, 47))
        self.turn_bar2.setMaximumSize(QtCore.QSize(40, 47))
        self.turn_bar3.setMaximumSize(QtCore.QSize(40, 47))

    def change_swerve_bar(self, level:int):
        if level == 0:
            self.swerve_bar1.setPixmap(self.grey_bar)
            self.swerve_bar2.setPixmap(self.grey_bar)
            self.swerve_bar3.setPixmap(self.bottom_bar)
        elif level == 1:
            self.swerve_bar1.setPixmap(self.grey_bar)
            self.swerve_bar2.setPixmap(self.medium_bar)
            self.swerve_bar3.setPixmap(self.bottom_bar)
        elif level == 2:
            self.swerve_bar1.setPixmap(self.top_bar)
            self.swerve_bar2.setPixmap(self.medium_bar)
            self.swerve_bar3.setPixmap(self.bottom_bar)
        self.swerve_bar1.setScaledContents(True)
        self.swerve_bar2.setScaledContents(True)
        self.swerve_bar3.setScaledContents(True)
        self.swerve_bar1.setMaximumSize(QtCore.QSize(40, 47))
        self.swerve_bar2.setMaximumSize(QtCore.QSize(40, 47))
        self.swerve_bar3.setMaximumSize(QtCore.QSize(40, 47))

    def change_brake_bar(self, level: int):
        if level == 0:
            self.brake_bar1.setPixmap(self.grey_bar)
            self.brake_bar2.setPixmap(self.grey_bar)
            self.brake_bar3.setPixmap(self.bottom_bar)
        elif level == 1:
            self.brake_bar1.setPixmap(self.grey_bar)
            self.brake_bar2.setPixmap(self.medium_bar)
            self.brake_bar3.setPixmap(self.bottom_bar)
        elif level == 2:
            self.brake_bar1.setPixmap(self.top_bar)
            self.brake_bar2.setPixmap(self.medium_bar)
            self.brake_bar3.setPixmap(self.bottom_bar)
        self.brake_bar1.setScaledContents(True)
        self.brake_bar2.setScaledContents(True)
        self.brake_bar3.setScaledContents(True)
        self.brake_bar1.setMaximumSize(QtCore.QSize(40, 47))
        self.brake_bar2.setMaximumSize(QtCore.QSize(40, 47))
        self.brake_bar3.setMaximumSize(QtCore.QSize(40, 47))



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.next_page.setText(_translate("MainWindow", "Next Page>>"))
        self.total_coins_img.setText(_translate("MainWindow", ""))
        self.total_coins_score.setText(_translate("MainWindow", "27"))
        self.total_coins.setText(_translate("MainWindow", "Total Coins"))
        self.trip_score_img.setText(_translate("MainWindow", ""))
        self.trip_score_score.setText(_translate("MainWindow", "91"))
        self.trip_score.setText(_translate("MainWindow", "Trip Score"))
        self.current_score.setText(_translate("MainWindow", "86"))
        self.current_score_text.setText(_translate("MainWindow", "Current Score"))



   # def runningave(self,):
