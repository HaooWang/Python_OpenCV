#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/4 16:55
# @Author  : HaoWANG
# @Site    : 
# @File    : 045. 拖动条.py
# @Software: PyCharm


import numpy as np
import cv2 as cv
def nothing(x):
    pass
# Create a black image, a window
img = cv.imread("../pictures/lena.png")
cv.namedWindow('image')
# create trackbars for color change
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)
# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'image',0,1,nothing)
while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    # get current positions of four trackbars
    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')
    s = cv.getTrackbarPos(switch,'image')
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
cv.destroyAllWindows()