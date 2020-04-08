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
        self.pie_widget.setMinimumSize(QtCore.QSize(300, 200))
        self.pie_widget.setObjectName("pie_widget")
        self.CurrentScore = QtWidgets.QLabel(self.pie_widget)
        self.CurrentScore.setGeometry(QtCore.QRect(110, 70, 91, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CurrentScore.sizePolicy().hasHeightForWidth())
        self.CurrentScore.setSizePolicy(sizePolicy)
        self.CurrentScore.setMinimumSize(QtCore.QSize(20, 20))
        self.CurrentScore.setMaximumSize(QtCore.QSize(300, 120))
        font = QtGui.QFont()
        font.setFamily("Brush Script Std")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.CurrentScore.setFont(font)
        self.CurrentScore.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentScore.setObjectName("CurrentScore")

        self.badge1 = QtWidgets.QLabel(self.graph_widget)
        self.badge1.setGeometry(QtCore.QRect(420, 60, 51, 51))
        self.badge1.setText("")
        self.badge1.setObjectName("badge1")

        self.badge2 = QtWidgets.QLabel(self.graph_widget)
        self.badge2.setGeometry(QtCore.QRect(510, 60, 51, 51))
        self.badge2.setText("")
        self.badge2.setObjectName("badge2")
        self.badge3 = QtWidgets.QLabel(self.graph_widget)
        self.badge3.setGeometry(QtCore.QRect(590, 60, 51, 51))
        self.badge3.setText("")
        self.badge3.setObjectName("badge3")


        self.CurrentScore_3 = QtWidgets.QLabel(self.pie_widget)
        self.CurrentScore_3.setGeometry(QtCore.QRect(20, 0, 300, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CurrentScore_3.sizePolicy().hasHeightForWidth())
        self.CurrentScore_3.setSizePolicy(sizePolicy)
        self.CurrentScore_3.setMinimumSize(QtCore.QSize(20, 20))
        self.CurrentScore_3.setMaximumSize(QtCore.QSize(300, 120))
        font = QtGui.QFont()
        font.setFamily("Brush Script Std")
        font.setPointSize(33)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.CurrentScore_3.setFont(font)
        self.CurrentScore_3.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentScore_3.setObjectName("CurrentScore_3")
        self.horizontalLayout_2.addWidget(self.pie_widget)
        self.verticalLayout.addWidget(self.graph_widget)

        pg.setConfigOption('background', '#17191A')


        self._badge1 = QtGui.QPixmap('icons/Badges/png/001-first-place.png')
        self._badge2 = QtGui.QPixmap('icons/Badges/png/002-silver-medal.png')
        self._badge3 = QtGui.QPixmap('icons/Badges/png/003-bronze-medal.png')

        self.badge1.setPixmap(self._badge1)
        self.badge1.setScaledContents(True)
        self.badge1.setMaximumSize(QtCore.QSize(80, 31))

        self.badge2.setPixmap(self._badge2)
        self.badge2.setScaledContents(True)
        self.badge2.setMaximumSize(QtCore.QSize(80, 31))

        self.badge3.setPixmap(self._badge3)
        self.badge3.setScaledContents(True)
        self.badge3.setMaximumSize(QtCore.QSize(80, 31))

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
        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        score1 = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]


        bonder = [20,50,50,20,20]
        b_hour_g = [5,5,7,7,5]
        b_hour_r = [1,1,5,5,1]

        self.plot = self.plot_widget.addPlot()

        self.label = pg.TextItem()
        self.plot.addItem(self.label)

        self.plot.showGrid(x=True, y=True, alpha=0.5)
        self.plot.plot(x=hour, y=score1, pen='r', name='score', symbolBrush=(255, 0, 0), )
        self.plot.plot(x=b_hour_g, y=bonder, pen='g', name='score',  )
        self.plot.setLabel(axis='left', text='score')
        self.plot.setLabel(axis='bottom', text='date')
        self.vLine = pg.InfiniteLine(angle=90, movable=False, )
        self.hLine = pg.InfiniteLine(angle=0, movable=False, )
        self.plot.addItem(self.vLine, ignoreBounds=True)
        self.plot.addItem(self.hLine, ignoreBounds=True)
        self.vb = self.plot.vb


    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.CurrentScore.setText(_translate("Dialog", "86"))
        self.CurrentScore_3.setText(_translate("Dialog", "Average Score:"))
        self.backBtn.setText(_translate("Dialog", "back"))

from pyqtgraph import PlotWidget
