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
from pyqtgraph import PlotWidget

import pyqtgraph as pg

# data里面必须有以下字段: 时间, 开盘价, 收盘价, 最低价, 最高价

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
        self.k_widget = QtWidgets.QWidget(self.graph_widget)
        self.k_widget.setMinimumSize(QtCore.QSize(500, 200))
        self.k_widget.setObjectName("pie_widget")
        self.k_layout = QtWidgets.QGridLayout()  # grid
        self.k_widget.setLayout(self.k_layout)  # candlestick
        self.k_plt = pg.PlotWidget()  # 实例化一个绘图部件
        self.k_layout.addWidget(self.k_plt)  # 添加绘图部件到K线图部件的网格布局层

        # 将上述部件添加到布局层中
        # self.main_layout.addWidget(self.stock_code, 0, 0, 1, 1)
        # self.main_layout.addWidget(self.option_sel, 0, 1, 1, 1)
        # self.main_layout.addWidget(self.que_btn, 0, 2, 1, 1)
        # self.main_layout.addWidget(self.k_widget, 1, 0, 3, 3)


        self.horizontalLayout_2.addWidget(self.k_widget)
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

        # self.pie_widget =  QtWidgets.QWidget(self.graph_widget)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.pie_widget.sizePolicy().hasHeightForWidth())
        # self.pie_widget.setSizePolicy(sizePolicy)
        # self.pie_widget.setMinimumSize(QtCore.QSize(0, 50))
        # self.pie_widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.k_widget.setObjectName("pie_widget")
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

        bonder = [20,50,50,20,20]
        b_hour_g = [5,5,7,7,5]
        b_hour_r = [1,1,5,5,1]
        # self.plot_widget.showGrid(x = True)
        # self.plot_widget.setXRange(0, 10, padding=0)
        # self.plot_widget.setYRange(20, 55, padding=0)
        #
        # self.plot_widget.plot(hour, score1, 'r')
        #
        # pg.setConfigOption('background', 'k')
        # pen = pg.mkPen(color=(255, 0, 0))
        # pg.setConfigOption('foreground', 'w')
        # pen2 = pg.mkPen(color=(0, 255, 0))
        pen_b = pg.mkPen(color=(0, 255, 0),width=5)
        # pen_r = pg.mkPen(color=(255, 0, 0),width=5)
        # self.plot_widget.plot(hour1, score21, name="Sensor 1",  pen=pen)
        # self.plot_widget.plot(hour3, score23, name="Sensor 1",  pen=pen)
        # self.plot_widget.plot(hour2, score22, name="Sensor 2",  pen=pen2)
        # self.plot_widget.plot(b_hour_g,bonder, name="Sensor 2",  pen=pen_b)
        # self.plot_widget.plot(b_hour_r,bonder, name="Sensor 2",  pen=pen_r)

        # data = ts.get_hist_data('sh', start='2017-10-01', end='2017-12-01').sort_index()
        # xdict = dict(enumerate(data.index))
        # axis_1 = [(i, list(data.index)[i]) for i in range(0, len(data.index), 5)]
        # stringaxis = pg.AxisItem(orientation='bottom')
        # stringaxis.setTicks([axis_1, xdict.items()])
        # self.plot_widget = pg.GraphicsWindow(title='plot gragh')
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

        # self.proxy = pg.SignalProxy(self.plot.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMoved)


        self.data = data
        # self.generatePicture()
        self.plot_k_line()


    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())


    def plot_k_line(self,code=None,start=None,end=None):
        self.data = np.array(data)

        # data = [[0, 10, 20, 9, 23], [1, 10, 20, 9, 23], [2, 10, 20, 9, 23], [3, 10, 20, 9, 23]]
        y_min = self.data[:,3].min()
        print(y_min)
        y_max = self.data[:,4].max()

        self.k_plt.plotItem.clear() # 清空绘图部件中的项
        # item = self.picture  # 生成蜡烛图数据
        item = CandlestickItem(self.data)  # 生成蜡烛图数据
        self.k_plt.addItem(item)  # 在绘图部件中添加蜡烛图项目
        self.k_plt.showGrid(x=True, y=True)  # 设置绘图部件显示网格线
        self.k_plt.setYRange(y_min,y_max)
        self.k_plt.setLabel(axis='left', text='score')  # 设置Y轴标签
        self.k_plt.setLabel(axis='bottom', text='date')  # 设置X轴标签
        self.label = pg.TextItem()  # 创建一个文本项
        self.k_plt.addItem(self.label)  # 在图形部件中添加文本项

        self.vLine = pg.InfiniteLine(angle=90, movable=False, )  # 创建一个垂直线条
        self.hLine = pg.InfiniteLine(angle=0, movable=False, )  # 创建一个水平线条
        self.k_plt.addItem(self.vLine, ignoreBounds=True)  # 在图形部件中添加垂直线条
        self.k_plt.addItem(self.hLine, ignoreBounds=True)  # 在图形部件中添加水平线条

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.backBtn.setText(_translate("Dialog", "back"))



# K线图绘制类
class CandlestickItem(pg.GraphicsObject):
    # 州的先生zmister.com
    def __init__(self, data):
        pg.GraphicsObject.__init__(self)
        self.data = data  # data里面必须有以下字段: 时间, 开盘价, 收盘价, 最低价, 最高价
        self.generatePicture()

    def generatePicture(self):
        self.picture = QtGui.QPicture() # 实例化一个绘图设备
        p = QtGui.QPainter(self.picture) # 在picture上实例化QPainter用于绘图
        p.setPen(pg.mkPen('w')) # 设置画笔颜色
        w = (self.data[1][0] - self.data[0][0]) / 3.
        for (t, open, close, min, max) in self.data:
            print(t, open, close, min, max)
            p.drawLine(QtCore.QPointF(t, min), QtCore.QPointF(t, max)) # 绘制线条
            if open > close: # 开盘价大于收盘价
                p.setBrush(pg.mkBrush('g')) # 设置画刷颜色为绿
            else:
                p.setBrush(pg.mkBrush('r')) # 设置画刷颜色为红
            p.drawRect(QtCore.QRectF(t - w, open, w * 2, close - open)) # 绘制箱子
        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())
