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

        pg.setConfigOption('background', '#17191A')

        self.pie_widget = QtWidgets.QWidget(self.graph_widget)
        self.acc_pic_coin = QtWidgets.QLabel(self.pie_widget)
        self.acc_pic_coin.setMargin(5)
        self._gold_coin = QtGui.QPixmap('icons/Badges/png/001-first-place.png')
        self.acc_pic_coin.setPixmap(self._gold_coin)
        self.acc_pic_coin.setScaledContents(True)
        self.acc_pic_coin.setMaximumSize(QtCore.QSize(80, 31))


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
        self.backBtn.setText(_translate("Dialog", "back"))



