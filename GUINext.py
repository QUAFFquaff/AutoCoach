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
from PyQt5.QtChart import *

class Ui_Dialog(object):
    windowMoved = QtCore.pyqtSignal(QtCore.QPoint)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(750, 500)
        self.back = QtWidgets.QFrame(Dialog)
        self.back.setGeometry(QtCore.QRect(9, 9, 731, 481))
        self.back.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.back.setFrameShadow(QtWidgets.QFrame.Raised)
        self.back.setObjectName("back")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.back)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.canvas = QtWidgets.QWidget(self.back)
        self.canvas.setMinimumSize(QtCore.QSize(0, 0))
        self.canvas.setObjectName("canvas")
        self.gridLayout = QtWidgets.QGridLayout(self.canvas)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2.addWidget(self.canvas)
        self.down = QtWidgets.QWidget(self.back)
        self.down.setMinimumSize(QtCore.QSize(0, 50))
        self.down.setMaximumSize(QtCore.QSize(16777215, 50))
        self.down.setObjectName("down")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.down)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.backBtn = QtWidgets.QPushButton(self.down)
        self.backBtn.setMaximumSize(QtCore.QSize(60, 16777215))
        self.backBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.backBtn.setAutoFillBackground(False)
        self.backBtn.setDefault(False)
        self.backBtn.setObjectName("backBtn")
        self.horizontalLayout.addWidget(self.backBtn)
        self.verticalLayout_2.addWidget(self.down)

        self.pie_widget =  QtWidgets.QWidget(self.back)
        self.down.setMinimumSize(QtCore.QSize(0, 50))
        self.down.setMaximumSize(QtCore.QSize(16777215, 50))
        # self.pie_widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pie_widget.setObjectName("pie_widget")
        # beautify window
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # hide the boarder
        self.setWindowOpacity(0.98)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # set transparent window

        # window move
        self.windowMoved.connect(self.move)  # move window

        self.backBtn.setFixedSize(60, 30)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pieseries = QPieSeries(self.pie_widget)  # define PieSeries
        self.pieseries.append("Jane", 1)  # insert
        self.pieseries.append("Joe", 2)
        self.pieseries.append("Andy", 3)
        self.pieseries.append("Barbara", 4)
        self.pieseries.append("Axel", 5)

        self.slice = self.pieseries.slices()[0]  # select one split
        self.slice.setExploded()  # set as exploded
        self.slice.setLabelVisible()  # Lable
        self.slice.setPen(QPen(Qt.darkGreen, 1))  # set pen
        self.slice.setBrush(Qt.green)

        self.chart = QChart()  # 定义QChart
        self.chart.addSeries(self.pieseries)  # 将 pieseries添加到chart里
        self.chart.setTitle("Simple piechart example")  # 设置char的标题
        self.chart.legend().hide()  # 将char的legend设置为隐藏

        self.charview = QChartView(self.chart, self.pie_widget)  # 定义charView窗口，添加chart元素，设置主窗口为父窗体，既将chartView嵌入到父窗体
        self.charview.setGeometry(0, 0, 50, 50)  # 设置charview在父窗口的大小、位置
        self.charview.setRenderHint(QPainter.Antialiasing)  # 设置抗锯齿
        self.charview.show()  # 将CharView窗口显示出来


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

