#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/4 16:42
# @Author  : HaoWANG
# @Site    : 
# @File    : 043.鼠标.py
# @Software: PyCharm

import numpy as np
import cv2 as cv
# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),10,(0,0,255),-1)
# Create a black image, a window and bind the function to window
img = cv.imread("")
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()