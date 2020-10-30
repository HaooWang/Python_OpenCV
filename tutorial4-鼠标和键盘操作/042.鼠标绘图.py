#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/4 16:41
# @Author  : HaoWANG
# @Site    : 
# @File    : 042.鼠标绘图.py
# @Software: PyCharm


import cv2 as cv
events = [i for i in dir(cv) if 'EVENT' in i]
print( events )

# result
# # ['EVENT_FLAG_ALTKEY',
# # 'EVENT_FLAG_CTRLKEY',
# # 'EVENT_FLAG_LBUTTON',
# # 'EVENT_FLAG_MBUTTON',
# # 'EVENT_FLAG_RBUTTON',
# # 'EVENT_FLAG_SHIFTKEY',
# # 'EVENT_LBUTTONDBLCLK',
# # 'EVENT_LBUTTONDOWN',
# # 'EVENT_LBUTTONUP',
# # 'EVENT_MBUTTONDBLCLK',
# # 'EVENT_MBUTTONDOWN',
# # 'EVENT_MBUTTONUP',
# # 'EVENT_MOUSEHWHEEL',
# # 'EVENT_MOUSEMOVE',
# # 'EVENT_MOUSEWHEEL',
# # 'EVENT_RBUTTONDBLCLK',
# # 'EVENT_RBUTTONDOWN',
# # 'EVENT_RBUTTONUP']
