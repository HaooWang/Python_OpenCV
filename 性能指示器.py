#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/4 17:07
# @Author  : HaoWANG
# @Site    : 
# @File    : 性能指示器.py
# @Software: PyCharm

import cv2 as cv
from platForm import img_path

e1 = cv.getTickCount()
src = cv.imread("{}/pictures/finger.jpg".format(img_path()))

kernel = 5
img = cv.medianBlur(src,3)
    
e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()
print( t )
cv.imshow("Image", img)
# Result I got is 0.521107655 seconds 