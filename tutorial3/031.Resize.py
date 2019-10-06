#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/5 3:09 PM
# @Author  : HaoWang
# @Site    : 
# @File    : 031.Transformation.py
# @Software: PyCharm

import numpy as np
import cv2 as cv

src = cv.imread('../pictures/coins.jpg')
# img = cv.GaussianBlur(src,(3,3),5)
img = cv.medianBlur(src,3)
cv.imshow("Src",src)
#
# res = cv.resize(img,None,fx=0.3, fy=0.3, interpolation = cv.INTER_CUBIC)


rows,cols = src[:,:,0].shape
# cols-1 and rows-1 are the coordinate limits.
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst = cv.warpAffine(src,M,(cols,rows))
cv.imshow("Rotation",dst)
cv.waitKey(0)
cv.destroyAllWindows()
#OR

# height, width = img.shape[:2]
#
# res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)