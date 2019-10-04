#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/4 17:07
# @Author  : HaoWANG
# @Site    : 
# @File    : 性能指示器.py
# @Software: PyCharm

import cv2 as cv

cv.namedWindow("Image",cv.WINDOW_NORMAL)
img = cv.imread('../pictures/lena.png')
img2 = cv.GaussianBlur(img,(5,5),5)
cv.imshow("Image",img)

e1 = cv.getTickCount()
for i in range(3,30,2):
    img1 = cv.medianBlur(img1,i)
    
e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()
print( t )
# Result I got is 0.521107655 seconds
cv.waitkey(0)