# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUINext_refer.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
import datetime
import traceback

from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtChart import *
import pyqtgraph as pg
import numpy as np
from PyQt5.QtGui import QIcon, QPalette, QBrush, QPixmap
from pyqtgraph import PlotWidget

import pyqtgraph as pg

data = [[0, 10, 20, 9, 30], [1, 50, 20, 9, 60], [2, 10, 20, 9, 23], [3, 10, 30, -10, 50] ,[4, 50, 20, 9, 55],[5, 35, 10, 5, 40],
        [6, 50, 20, 9, 55], [7, 2, 20, -20, 55], [8, 50, 20, 9, 55], [9, 40, 30, 9, 70]]
class Ui_Dialog(object):
    windowMoved = QtCore.pyqtSignal(QtCore.QPoint)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(750, 500)
        self.back = QtWidgets.QFrame(Dialog)
        self.back.setGeometry(QtCore.QRect(9, 9, 741, 491))
        self.back.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.back.setFrameShadow(QtWidgets.QFrame.Raised)
        self.back.setObjectName("back")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.back)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.canvas = QtWidgets.QWidget(self.back)
        self.canvas.setMinimumSize(QtCore.QSize(0, 0))
        self.canvas.setObjectName("canvas")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.canvas)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graph_widget = QtWidgets.QWidget(self.canvas)
        self.graph_widget.setObjectName("graph_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.graph_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pie_widget = QtWidgets.QWidget(self.graph_widget)
        self.pie_widget.setMinimumSize(QtCore.QSize(650, 200))
        self.pie_widget.setObjectName("pie_widget")


        self.graph_widget.setStyleSheet('QWidget {background-color: #17191a; color: #46b8ff;}')

        self.summary_text = QtWidgets.QLabel(self.pie_widget)
        self.summary_text.setGeometry(QtCore.QRect(230, 0, 231, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.summary_text.sizePolicy().hasHeightForWidth())
        self.summary_text.setSizePolicy(sizePolicy)
        self.summary_text.setMinimumSize(QtCore.QSize(20, 20))
        self.summary_text.setMaximumSize(QtCore.QSize(300, 120))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.summary_text.setFont(font)
        self.summary_text.setAlignment(QtCore.Qt.AlignCenter)
        self.summary_text.setObjectName("summary_text")
        self.Total_coins_text = QtWidgets.QLabel(self.pie_widget)
        self.Total_coins_text.setGeometry(QtCore.QRect(530, 70, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Total_coins_text.sizePolicy().hasHeightForWidth())
        self.Total_coins_text.setSizePolicy(sizePolicy)
        self.Total_coins_text.setMinimumSize(QtCore.QSize(20, 20))
        self.Total_coins_text.setMaximumSize(QtCore.QSize(300, 120))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Total_coins_text.setFont(font)
        self.Total_coins_text.setAlignment(QtCore.Qt.AlignCenter)
        self.Total_coins_text.setObjectName("Total_coins_text")
        self.Coins_earned_text = QtWidgets.QLabel(self.pie_widget)
        self.Coins_earned_text.setGeometry(QtCore.QRect(360, 70, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Coins_earned_text.sizePolicy().hasHeightForWidth())
        self.Coins_earned_text.setSizePolicy(sizePolicy)
        self.Coins_earned_text.setMinimumSize(QtCore.QSize(20, 20))
        self.Coins_earned_text.setMaximumSize(QtCore.QSize(300, 120))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Coins_earned_text.setFont(font)
        self.Coins_earned_text.setAlignment(QtCore.Qt.AlignCenter)
        self.Coins_earned_text.setObjectName("Coins_earned_text")
        self.coins_earned_score = QtWidgets.QLabel(self.pie_widget)
        self.coins_earned_score.setGeometry(QtCore.QRect(380, 120, 101, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coins_earned_score.sizePolicy().hasHeightForWidth())
        self.coins_earned_score.setSizePolicy(sizePolicy)
        self.coins_earned_score.setMinimumSize(QtCore.QSize(20, 20))
        self.coins_earned_score.setMaximumSize(QtCore.QSize(300, 120))
        font = QtGui.QFont()
        font.setFamily("Brush Script Std")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.coins_earned_score.setFont(font)
        self.coins_earned_score.setAlignment(QtCore.Qt.AlignCenter)
        self.coins_earned_score.setObjectName("coins_earned_score")
        self.total_coins_score = QtWidgets.QLabel(self.pie_widget)
        self.total_coins_score.setGeometry(QtCore.QRect(550, 130, 81, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.total_coins_score.sizePolicy().hasHeightForWidth())
        self.total_coins_score.setSizePolicy(sizePolicy)
        self.total_coins_score.setMinimumSize(QtCore.QSize(20, 20))
        self.total_coins_score.setMaximumSize(QtCore.QSize(300, 120))
        font = QtGui.QFont()
        font.setFamily("Brush Script Std")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.total_coins_score.setFont(font)
        self.total_coins_score.setAlignment(QtCore.Qt.AlignCenter)
        self.total_coins_score.setObjectName("tota_coins_score")
        self.trip_score_text = QtWidgets.QLabel(self.pie_widget)
        self.trip_score_text.setGeometry(QtCore.QRect(190, 70, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trip_score_text.sizePolicy().hasHeightForWidth())
        self.trip_score_text.setSizePolicy(sizePolicy)
        self.trip_score_text.setMinimumSize(QtCore.QSize(20, 20))
        self.trip_score_text.setMaximumSize(QtCore.QSize(300, 120))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.trip_score_text.setFont(font)
        self.trip_score_text.setAlignment(QtCore.Qt.AlignCenter)
        self.trip_score_text.setObjectName("trip_score_text")
        self.trip_score_score = QtWidgets.QLabel(self.pie_widget)
        self.trip_score_score.setGeometry(QtCore.QRect(210, 120, 101, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trip_score_score.sizePolicy().hasHeightForWidth())
        self.trip_score_score.setSizePolicy(sizePolicy)
        self.trip_score_score.setMinimumSize(QtCore.QSize(20, 20))
        self.trip_score_score.setMaximumSize(QtCore.QSize(300, 120))
        font = QtGui.QFont()
        font.setFamily("Brush Script Std")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.trip_score_score.setFont(font)
        self.trip_score_score.setAlignment(QtCore.Qt.AlignCenter)
        self.trip_score_score.setObjectName("trip_score_score")
        self.Personal_score_text = QtWidgets.QLabel(self.pie_widget)
        self.Personal_score_text.setGeometry(QtCore.QRect(30, 70, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Personal_score_text.sizePolicy().hasHeightForWidth())
        self.Personal_score_text.setSizePolicy(sizePolicy)
        self.Personal_score_text.setMinimumSize(QtCore.QSize(20, 20))
        self.Personal_score_text.setMaximumSize(QtCore.QSize(300, 120))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Personal_score_text.setFont(font)
        self.Personal_score_text.setAlignment(QtCore.Qt.AlignCenter)
        self.Personal_score_text.setObjectName("Personal_score_text")
        self.personal_score_score = QtWidgets.QLabel(self.pie_widget)
        self.personal_score_score.setGeometry(QtCore.QRect(50, 120, 81, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.personal_score_score.sizePolicy().hasHeightForWidth())
        self.personal_score_score.setSizePolicy(sizePolicy)
        self.personal_score_score.setMinimumSize(QtCore.QSize(20, 20))
        self.personal_score_score.setMaximumSize(QtCore.QSize(300, 120))
        font = QtGui.QFont()
        font.setFamily("Brush Script Std")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.personal_score_score.setFont(font)
        self.personal_score_score.setAlignment(QtCore.Qt.AlignCenter)
        self.personal_score_score.setObjectName("personal_score_score")
        self.Badge_img = QtWidgets.QLabel(self.pie_widget)
        self.Badge_img.setGeometry(QtCore.QRect(55, 20, 91, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Badge_img.sizePolicy().hasHeightForWidth())
        self.Badge_img.setSizePolicy(sizePolicy)
        self.Badge_img.setMinimumSize(QtCore.QSize(20, 20))
        self.Badge_img.setMaximumSize(QtCore.QSize(300, 120))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Badge_img.setFont(font)
        self.Badge_img.setText("")
        self.Badge_img.setAlignment(QtCore.Qt.AlignCenter)
        self.Badge_img.setObjectName("Badge_img")
        self.Coin_img = QtWidgets.QLabel(self.pie_widget)
        self.Coin_img.setGeometry(QtCore.QRect(550, 20, 91, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Coin_img.sizePolicy().hasHeightForWidth())
        self.Coin_img.setSizePolicy(sizePolicy)
        self.Coin_img.setMinimumSize(QtCore.QSize(20, 20))
        self.Coin_img.setMaximumSize(QtCore.QSize(300, 120))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Coin_img.setFont(font)
        self.Coin_img.setText("")
        self.Coin_img.setAlignment(QtCore.Qt.AlignCenter)
        self.Coin_img.setObjectName("Coin_img")
        self.horizontalLayout_2.addWidget(self.pie_widget)
        self.verticalLayout.addWidget(self.graph_widget)

        self._badge1 = QtGui.QPixmap('icons/Badges/png/020-badge.png')
        self._badge2 = QtGui.QPixmap('icons/events/Less_Coins.png')
        # self._badge3 = QtGui.QPixmap('icons/Badges/png/003-bronze-medal.png')

        self.Badge_img.setPixmap(self._badge1)
        self.Badge_img.setScaledContents(True)
        self.Badge_img.setMaximumSize(QtCore.QSize(60, 90))

        self.Coin_img.setPixmap(self._badge2)
        self.Coin_img.setScaledContents(True)
        self.Coin_img.setMaximumSize(QtCore.QSize(60,90))

        self.coins_earned_score.setStyleSheet('QWidget {background-color: #17191a; color: yellow;}')
        self.total_coins_score.setStyleSheet('QWidget {background-color: #17191a; color: grey;}')
        self.trip_score_score.setStyleSheet('QWidget {background-color: #17191a; color: yellow;}')
        self.personal_score_score.setStyleSheet('QWidget {background-color: #17191a; color: grey;}')
        self.horizontalLayout_2.addWidget(self.pie_widget)
        self.verticalLayout.addWidget(self.graph_widget)

        pg.setConfigOption('background', '#17191A')



        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.graph_widget)
        # self.plot_widget = PlotWidget(self.canvas)
        self.plot_widget = pg.GraphicsWindow(title='title')
        self.plot_widget.setObjectName("plot_widget")
        self.verticalLayout.addWidget(self.plot_widget)
        self.verticalLayout_2.addWidget(self.canvas)
        self.down = QtWidgets.QWidget(self.back)
        self.down.setMinimumSize(QtCore.QSize(0, 50))
        self.down.setMaximumSize(QtCore.QSize(16777215, 50))
        self.down.setObjectName("down")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.down)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.backBtn = QtWidgets.QPushButton(self.down)
        self.backBtn.setMaximumSize(QtCore.QSize(60, 16777215))
        self.backBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.backBtn.setAutoFillBackground(False)
        self.backBtn.setDefault(False)
        self.backBtn.setObjectName("backBtn")
        self.horizontalLayout.addWidget(self.backBtn)
        self.verticalLayout_2.addWidget(self.down)

        # self.graph_widget = QtWidgets.QWidget(self.canvas)
        self.graph_widget.setObjectName("graph_widget")


        # window move
        self.windowMoved.connect(self.move)  # move window

        self.backBtn.setFixedSize(60, 30)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)




        # self.plot_widget = PlotWidget(self.canvas)
        self.plot_widget.setObjectName("plot_widget")
        hour = np.arange(30)
        score1 = [20, 21, 22, 19, 66, 65, 59, 89, 91, 90,
                  60, 50, 60, 66, 41, 49, 68, 69, 80, 81,
                  60, 69, 49, 80, 70, 79, 82, 83, 89, 90]


        bonder = [20,50,50,20,20]
        b_hour_g = [5,5,7,7,5]
        b_hour_r = [1,1,5,5,1]

        self.plot = self.plot_widget.addPlot()

        self.label = pg.TextItem()
        self.plot.addItem(self.label)

        self.plot.showGrid(x=True, y=True, alpha=0.5)

        windowmean = self.get_mean(5,score1)
        print(windowmean)

        self.plot.plot(x=hour, y=score1, pen='w', name='score', symbolBrush=(0, 0, 0), symbolSize = 5 )
        # self.plot.plot(x=b_hour_g, y=bonder, pen='g', name='score',  )
        # self.plot.setLabel(axis='left', text='score')
        # self.plot.setLabel(axis='bottom', text='date')
        # self.vLine = pg.InfiniteLine(angle=90, movable=False, )
        # self.hLine = pg.InfiniteLine(angle=0, movable=False, )
        # self.plot.addItem(self.vLine, ignoreBounds=True)
        # self.plot.addItem(self.hLine, ignoreBounds=True)
        # self.vb = self.plot.vb
        self.set_average(score1)
        self.plot_graph(hour,windowmean)
    def set_average(self,scores):
        self.trip_average_score.setText(str(round(np.mean(scores), 1)))

    def get_mean(self,windowsize,score):
        temp = [score[0] for _ in range(windowsize-1)]
        temp+=score
        print(temp)
        windowmean = [np.mean(temp[i:i+windowsize])for i in range(len(score))]
        return windowmean

    def plot_graph(self, time, score):
        symbolSize = 2
        for i in range(1,len(score)):

            if score[i]-score[i-1]>1:
                self.plot.plot(x=time[i-1:i+1], y=score[i-1:i+1], pen='g', name='score', symbolBrush=(0,0,0), symbolSize = symbolSize )
            elif score[i]-score[i-1]<-1:
                self.plot.plot(x=time[i-1:i+1], y=score[i-1:i+1], pen='r', name='score', symbolBrush=(0,0,0), symbolSize = symbolSize )
            else:
                self.plot.plot(x=time[i-1:i+1], y=score[i-1:i+1], pen='y', name='score', symbolBrush=(0,0,0), symbolSize = symbolSize )

        self.plot.setLabel(axis='left', text='score')
        self.plot.setLabel(axis='bottom', text='time')
        self.vb = self.plot.vb
        # threshold = 15
        # start = 0 # []
        # for i in range(len(score)):
        #     mu = np.mean(score[start:i+1])
        #     sigma = np.var(score[start:i+1])/(i-start)
        #     if i == len(score)-1 or sigma>threshold:
        #         color = self.set_pen_color(mu)
        #         print('hey')
        #         print('sigma: ',sigma,'threshold:',threshold,'color',color)
        #         self.plot.plot(x=time[start:i+1], y=score[start:i+1], pen=color, name='score', symbolBrush=(0,255,0), )
        #         start = i
        # self.plot.setLabel(axis='left', text='score')
        # self.plot.setLabel(axis='bottom', text='time')
        # self.vb = self.plot.vb

############ using variance and mean to cluster

    #     self.set_average(score1)
    def set_average(self,scores):
        pass
        # self.trip_average_score.setText(str(round(np.mean(scores), 1)))
    #
    # def plot_graph(self,time,score):
    #     threshold = 15
    #     start = 0 # []
    #     for i in range(len(score)):
    #         mu = np.mean(score[start:i+1])
    #         sigma = np.var(score[start:i+1])/(i-start)
    #         if i == len(score)-1 or sigma>threshold:
    #             color = self.set_pen_color(mu)
    #             print('hey')
    #             print('sigma: ',sigma,'threshold:',threshold,'color',color)
    #             self.plot.plot(x=time[start:i+1], y=score[start:i+1], pen=color, name='score', symbolBrush=(0,255,0), )
    #             start = i
    #     self.plot.setLabel(axis='left', text='score')
    #     self.plot.setLabel(axis='bottom', text='time')
    #     self.vb = self.plot.vb
############ using variance and mean to cluster ↑

    def set_pen_color(self,mu):
        print(mu)
        threshold_low = 60
        threshold_high = 80
        if mu<=threshold_low:
            return 'r'
        if threshold_low<mu<threshold_high:
            return 'y'
        if threshold_high<= mu:
            return 'g'



    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())

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

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.summary_text.setText(_translate("Dialog", "Summary"))
        self.Total_coins_text.setText(_translate("Dialog", "Total Coins"))
        self.Coins_earned_text.setText(_translate("Dialog", "Coins Earned"))
        self.coins_earned_score.setText(_translate("Dialog", "+9"))
        self.total_coins_score.setText(_translate("Dialog", "86"))
        self.trip_score_text.setText(_translate("Dialog", "Trip Score"))
        self.trip_score_score.setText(_translate("Dialog", "86"))
        self.Personal_score_text.setText(_translate("Dialog", "Personal Score"))
        self.personal_score_score.setText(_translate("Dialog", "91"))
        self.backBtn.setText(_translate("Dialog", "back"))

from pyqtgraph import PlotWidget
