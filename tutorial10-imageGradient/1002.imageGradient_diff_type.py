#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 14:27
# @Author  : HaoWANG
# @Site    : 
# @File    : 1002.imageGradient_diff_type.py
# @Software: PyCharm


import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('../pictures/google.png',0)
# Output dtype = cv.CV_8U
sobelx8u = cv.Sobel(img,cv.CV_8U,1,0,ksize=7)

# Output dtype = cv.CV_64F. Then take its absolute and convert to cv.CV_8U
sobelx64f = cv.Sobel(img,cv.CV_64F,1,0,ksize=7)

# np.absoluate() func
abs_sobel64f = np.absolute(sobelx64f)
# np.uint8() 强制类型装换
sobel_8u = np.uint8(abs_sobel64f)

# matplotpy
plt.subplot(1,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(sobelx8u,cmap = 'gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(sobel_8u,cmap = 'gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])
# plt.show()
plt.show()