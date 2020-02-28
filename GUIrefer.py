# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIrefer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
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
        self.close = QtWidgets.QPushButton(self.bar)
        self.close.setMaximumSize(QtCore.QSize(30, 20))
        self.close.setText("")
        self.close.setObjectName("close")
        self.horizontalLayout.addWidget(self.close)
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
        self.next_page.setMaximumSize(QtCore.QSize(70, 30))
        self.next_page.setObjectName("next_page")
        self.horizontalLayout.addWidget(self.next_page)
        self.verticalLayout.addWidget(self.bar)
        self.Menu = QtWidgets.QGridLayout()
        self.Menu.setVerticalSpacing(6)
        self.Menu.setObjectName("Menu")
        self.down = QtWidgets.QWidget(self.centralwidget)
        self.down.setMinimumSize(QtCore.QSize(0, 130))
        self.down.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.down.setObjectName("down")
        self.gridLayout_down = QtWidgets.QGridLayout(self.down)
        self.gridLayout_down.setHorizontalSpacing(5)
        self.gridLayout_down.setObjectName("gridLayout_down")
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
        self.gridLayout_down.addWidget(self.CurrentScore, 0, 1, 1, 1)
        self.TotalScore = QtWidgets.QLabel(self.down)
        self.TotalScore.setMinimumSize(QtCore.QSize(0, 0))
        self.TotalScore.setMaximumSize(QtCore.QSize(250, 120))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(15)
        font.setKerning(True)
        self.TotalScore.setFont(font)
        self.TotalScore.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.TotalScore.setAlignment(QtCore.Qt.AlignCenter)
        self.TotalScore.setObjectName("TotalScore")
        self.gridLayout_down.addWidget(self.TotalScore, 0, 2, 1, 1)
        self.Menu.addWidget(self.down, 5, 0, 1, 1)
        self.up = QtWidgets.QWidget(self.centralwidget)
        self.up.setMinimumSize(QtCore.QSize(0, 300))
        self.up.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.up.setObjectName("up")
        self.gridLayout_up = QtWidgets.QGridLayout(self.up)
        self.gridLayout_up.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_up.setSpacing(0)
        self.gridLayout_up.setObjectName("gridLayout_up")
        self.swerve_bar = QtWidgets.QWidget(self.up)
        self.swerve_bar.setMaximumSize(QtCore.QSize(80, 220))
        self.swerve_bar.setObjectName("swerve_bar")
        self.verticalLayout_swerve = QtWidgets.QVBoxLayout(self.swerve_bar)
        self.verticalLayout_swerve.setContentsMargins(15, 0, 15, 0)
        self.verticalLayout_swerve.setSpacing(0)
        self.verticalLayout_swerve.setObjectName("verticalLayout_swerve")
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
        self.swerve_icon = QtWidgets.QLabel(self.swerve_bar)
        self.swerve_icon.setMinimumSize(QtCore.QSize(20, 20))
        self.swerve_icon.setMaximumSize(QtCore.QSize(20, 20))
        self.swerve_icon.setText("")
        self.swerve_icon.setObjectName("swerve_icon")
        self.verticalLayout_swerve.addWidget(self.swerve_icon, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_up.addWidget(self.swerve_bar, 1, 6, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_up.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_up.addItem(spacerItem2, 1, 4, 1, 1)
        self.backCircle = QtWidgets.QWidget(self.up)
        self.backCircle.setMinimumSize(QtCore.QSize(50, 50))
        self.backCircle.setMaximumSize(QtCore.QSize(320, 320))
        self.backCircle.setObjectName("backCircle")
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
        self.gridLayout_up.addWidget(self.backCircle, 1, 3, 2, 1)
        self.brake_bar = QtWidgets.QWidget(self.up)
        self.brake_bar.setMaximumSize(QtCore.QSize(80, 220))
        self.brake_bar.setObjectName("brake_bar")
        self.verticalLayout_break = QtWidgets.QVBoxLayout(self.brake_bar)
        self.verticalLayout_break.setContentsMargins(15, 0, 15, 0)
        self.verticalLayout_break.setSpacing(0)
        self.verticalLayout_break.setObjectName("verticalLayout_break")
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
        self.brake_icon = QtWidgets.QLabel(self.brake_bar)
        self.brake_icon.setMinimumSize(QtCore.QSize(20, 20))
        self.brake_icon.setMaximumSize(QtCore.QSize(20, 20))
        self.brake_icon.setObjectName("brake_icon")
        self.verticalLayout_break.addWidget(self.brake_icon, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_up.addWidget(self.brake_bar, 1, 1, 1, 1)
        self.brake_level = QtWidgets.QWidget(self.up)
        self.brake_level.setMaximumSize(QtCore.QSize(80, 35))
        self.brake_level.setObjectName("brake_level")
        self.gridLayout_up.addWidget(self.brake_level, 2, 1, 1, 1)
        self.turn_level = QtWidgets.QWidget(self.up)
        self.turn_level.setMaximumSize(QtCore.QSize(80, 35))
        self.turn_level.setObjectName("turn_level")
        self.gridLayout_up.addWidget(self.turn_level, 2, 5, 1, 1)
        self.turn_bar = QtWidgets.QWidget(self.up)
        self.turn_bar.setMaximumSize(QtCore.QSize(80, 220))
        self.turn_bar.setObjectName("turn_bar")
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
        self.turn_icon = QtWidgets.QLabel(self.turn_bar)
        self.turn_icon.setMinimumSize(QtCore.QSize(20, 20))
        self.turn_icon.setMaximumSize(QtCore.QSize(20, 20))
        self.turn_icon.setText("")
        self.turn_icon.setObjectName("turn_icon")
        self.verticalLayout_turn.addWidget(self.turn_icon, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_up.addWidget(self.turn_bar, 1, 5, 1, 1)
        self.acc_level = QtWidgets.QWidget(self.up)
        self.acc_level.setMaximumSize(QtCore.QSize(80, 35))
        self.acc_level.setObjectName("acc_level")
        self.gridLayout_up.addWidget(self.acc_level, 2, 0, 1, 1)
        self.swerve_level = QtWidgets.QWidget(self.up)
        self.swerve_level.setMaximumSize(QtCore.QSize(80, 35))
        self.swerve_level.setObjectName("swerve_level")
        self.gridLayout_up.addWidget(self.swerve_level, 2, 6, 1, 1)
        self.acc_bar = QtWidgets.QWidget(self.up)
        self.acc_bar.setMaximumSize(QtCore.QSize(80, 220))
        self.acc_bar.setObjectName("acc_bar")
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
        self.acc_icon = QtWidgets.QLabel(self.acc_bar)
        self.acc_icon.setMinimumSize(QtCore.QSize(20, 20))
        self.acc_icon.setMaximumSize(QtCore.QSize(20, 20))
        self.acc_icon.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.acc_icon.setAutoFillBackground(False)
        self.acc_icon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.acc_icon.setText("")
        self.acc_icon.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.acc_icon.setObjectName("acc_icon")
        self.verticalLayout_acc.addWidget(self.acc_icon, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_up.addWidget(self.acc_bar, 1, 0, 1, 1)
        self.Menu.addWidget(self.up, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(10)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.Menu.addWidget(self.line, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.Menu)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.next_page.setText(_translate("MainWindow", "Next Page"))
        self.CurrentScore.setText(_translate("MainWindow", "86"))
        self.TotalScore.setText(_translate("MainWindow", "1240 points"))
        self.brake_icon.setText(_translate("MainWindow", "l"))
from pyqtgraph import PlotWidget
