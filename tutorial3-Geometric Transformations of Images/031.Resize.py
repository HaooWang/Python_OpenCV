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

# cols-1 and rows-1 are the coordinate limits.
rows,cols = src[:,:,0].shape

# 这里的第一个参数为旋转中心，第二个为旋转角度，第三个为旋转后的缩放因子
# 可以通过设置旋转中心，缩放因子，以及窗口大小来防止旋转后超出边界的问题
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),45,0.56)
dst = cv.warpAffine(src,M,(cols,rows)) # 第三个参数是输出图像的尺寸中心
cv.imshow("Rotation",dst)
cv.waitKey(0)
cv.destroyAllWindows()
#OR

# height, width = img.shape[:2]
#
# res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)