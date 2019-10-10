#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 14:03
# @Author  : HaoWANG
# @Site    : 
# @File    : 1001. ImageGradient.py
# @Software: PyCharm


import numpy as np
import cv2 as cv

from matplotlib import pyplot as plt

img = cv.imread('../pictures/google.png',0)
# laplacian gradient
laplacian = cv.Laplacian(img,cv.CV_64F)

# Sobel gradient of X and Y
sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=11)
sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=11)

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()