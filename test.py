
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2/24/2020 12:58
# @Author  : Haoyu Lyu
# @File    : test.py
# @Software: PyCharm


import pyqtgraph as pg

## Switch to using white background and black foreground
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')

## The following plot has inverted colors
pg.plot([1,4,2,3,5])
pg.show()