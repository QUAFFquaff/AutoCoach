# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUINext_refer.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.backBtn.setText(_translate("Dialog", "back"))
from pyqtgraph import PlotWidget
