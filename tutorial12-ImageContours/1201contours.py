# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/10/30 17:10
# @Author  : HaoWang
# @Site    : HongKong, China
# @project : $[PROJECT_NAME]
# @File    : 1201contours.py.py
# @Software: PyCharm
# @license: haowanghk@gmail.com 
"""


import numpy as np
import cv2

im = cv2.imread('pictures/coins.jpg')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# draw contours
cont_img = cv2.drawContours(im, contours, -1, (0,255,0), 3)

cv2.imshow("Original Image",cont_img)
# cv2.imshow("Binary Image",im2)

print("thresh",ret)
# thresh 127.0

print("contours:",contours)
print(np.shape(contours))
# (579,)

cv2.waitKey(0)

cv2.destroyAllWindows()
