# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/10/6 16:06
# @Author  : HaoWang
# @Site    : HongKong, China
# @project : $[PROJECT_NAME]
# @File    : 0702.Adaptive Thresholding.py
# @Software: PyCharm
# @license: haowanghk@gmail.com 
"""

# import packages
import cv2

import numpy as np

from matplotlib import pyplot as plt

# reading image
img = cv2.imread('../pictures/lena.png', 0)

img = cv2.medianBlur(img, 7)

# simple thresholding
ret, th1 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

# adaptive thresholding with mean para
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \

cv2.THRESH_BINARY, 11, 2)

# adaptive thresholding with gaussian para
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \

cv2.THRESH_BINARY, 11, 2)

# show images
titles = ['Original Image', 'Global Thresholding (v = 150)',
                      'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']

images = [img, th1, th2, th3]

for i in range(4):

    plt.subplot(2, 2, i +1 ), plt.imshow(images[i], 'gray')

    plt.title(titles[i])

plt.xticks([]), plt.yticks([])

plt.show()