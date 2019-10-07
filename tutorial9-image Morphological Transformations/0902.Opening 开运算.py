# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/10/7 11:20
# @Author  : HaoWang
# @Site    : HongKong, China
# @project : $[PROJECT_NAME]
# @File    : 0902.Opening 开运算.py
# @Software: PyCharm
# @license: haowanghk@gmail.com 
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


src = cv.imread("../pictures/binary.png",0)
noi_src = cv.imread("../pictures/closing.jpg",0)

# erosion
kernel = np.ones((9,9), np.uint8)
erosion = cv.erode(src=src,kernel=kernel, iterations=1)

# dilation
dilation = cv.dilate(src, kernel,iterations =1 )

# Opening Alog
opening = cv.morphologyEx(noi_src, cv.MORPH_OPEN, kernel)

# Closing
closing = cv.morphologyEx(noi_src, cv.MORPH_CLOSE, kernel)

# gradient
gradient = cv.morphologyEx(closing, cv.MORPH_GRADIENT, kernel)

# tophat
tophat = cv.morphologyEx(src, cv.MORPH_TOPHAT, kernel)

# blackhat
blackhat = cv.morphologyEx(src, cv.MORPH_BLACKHAT, kernel)
plt.subplot(131),plt.imshow(src),plt.title("Original Image : "+ str(np.shape(src)))
plt.subplot(132),plt.imshow(erosion), plt.title("Erosion Image " )
plt.subplot(133), plt.imshow(blackhat), plt.title("blackhat " )

plt.show()

# plt.subplot(231), plt.imshow(noi_src), plt.title("Original Noisy Image " + str(np.shape(noi_src)) )
# plt.subplot(232), plt.imshow(closing), plt.title("closing ")
# plt.subplot(233), plt.imshow(gradient), plt.title("gradient ")
# plt.show()