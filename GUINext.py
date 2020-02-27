# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUINext_refer.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# from PyQt5.QtChart import *
from pyqtgraph import PlotWidget

import pyqtgraph as pg

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
        self.horizontalLayout_2.addWidget(self.pie_widget)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.graph_widget)
        self.plot_widget = PlotWidget(self.canvas)
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

        # self.pie_widget =  QtWidgets.QWidget(self.graph_widget)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.pie_widget.sizePolicy().hasHeightForWidth())
        # self.pie_widget.setSizePolicy(sizePolicy)
        # self.pie_widget.setMinimumSize(QtCore.QSize(0, 50))
        # self.pie_widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pie_widget.setObjectName("pie_widget")
        # self.pie_widget.setStyleSheet("#pie_widget{background-color: yellow}")
        # beautify window
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # hide the boarder
        self.setWindowOpacity(0.98)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # set transparent window

        # window move
        self.windowMoved.connect(self.move)  # move window

        self.backBtn.setFixedSize(60, 30)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # self.pieseries = QPieSeries(self.pie_widget)  # define PieSeries
        # self.pieseries.append("Jane", 1)  # insert
        # self.pieseries.append("Joe", 2)
        # self.pieseries.append("Andy", 3)
        # self.pieseries.append("Barbara", 4)
        # self.pieseries.append("Axel", 5)
        #
        # self.slice = self.pieseries.slices()[0]  # select one split
        # self.slice.setExploded()  # set as exploded
        # self.slice.setLabelVisible()  # Lable
        # self.slice.setPen(QPen(Qt.darkGreen, 1))  # set pen
        # self.slice.setBrush(Qt.green)
        #
        # self.chart = QChart()
        # self.chart.addSeries(self.pieseries)
        # self.chart.setTitle("Simple piechart example")
        # self.chart.legend().hide()
        #
        # self.charview = QChartView(self.chart, self.pie_widget)  # define charView，add chart item，set parent window
        # self.charview.setGeometry(0, 0, 300, 200)
        # self.charview.setRenderHint(QPainter.Antialiasing)
        # self.charview.show()



        # self.plot_widget = PlotWidget(self.canvas)
        self.plot_widget.setObjectName("plot_widget")
        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        score1 = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        score2 = [50,35,44,22,38,32,27,38,32,44]
        hour1 = [1, 2, 3, 4, 5]
        score21 = [50, 35, 44, 22, 38]
        hour2 = [5, 6, 7]
        score22 = [38,41,27]
        hour3 = [7, 8, 9, 10]
        score23 = [27,38,32,44]

        bonder = [0,100,100,0,0]
        b_hour_g = [5,5,7.5,7.5,5]

        self.plot_widget.showGrid(x = True)
        self.plot_widget.setXRange(0, 10, padding=0)
        self.plot_widget.setYRange(20, 55, padding=0)

        self.plot_widget.plot(hour, score1, 'r')

        pg.setConfigOption('background', 'k')
        pen = pg.mkPen(color=(255, 0, 0))
        pg.setConfigOption('foreground', 'w')
        pen2 = pg.mkPen(color=(0, 255, 0))
        pen_b = pg.mkPen(color=(0, 255, 0),width=5)
        # self.plot_widget.plot(hour, score1, name="Sensor 1",  pen=pen)
        # self.plot_widget.plot(hour, score2, name="Sensor 2",  pen=pen2)
        self.plot_widget.plot(hour1, score21, name="Sensor 1",  pen=pen)
        self.plot_widget.plot(hour3, score23, name="Sensor 1",  pen=pen)
        self.plot_widget.plot(hour2, score22, name="Sensor 2",  pen=pen2)
        self.plot_widget.plot(b_hour_g,bonder, name="Sensor 2",  pen=pen_b)

    # def plot(self, x, y, plotname, color):
    #     pen = pg.mkPen(color=color)
    #     self.graphWidget.plot(x, y, name=plotname, pen=pen, symbol='+', symbolSize=30, symbolBrush=(color))

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
        self.backBtn.setText(_translate("Dialog", "back"))

