# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/10/6 15:28
# @Author  : HaoWang
# @Site    : HongKong, China
# @project : $[PROJECT_NAME]
# @File    : 0701.Simple Thresholding.py
# @Software: PyCharm
# @license: haowanghk@gmail.com 
"""

import cv2

import numpy as np

from matplotlib import pyplot as plt


# reading the input image
img = cv2.imread('../pictures/rice.png', 0)

# applying the simple thresholding method to segmente the image by using diff param
ret, thresh1 = cv2.threshold(img, 20, 255, cv2.THRESH_BINARY)

ret, thresh2 = cv2.threshold(img, 20, 255, cv2.THRESH_BINARY_INV)

ret, thresh3 = cv2.threshold(img, 20, 255, cv2.THRESH_TRUNC)

ret, thresh4 = cv2.threshold(img, 20, 255, cv2.THRESH_TOZERO)

ret, thresh5 = cv2.threshold(img, 20, 255, cv2.THRESH_TOZERO_INV)


# show the image tital and image coordination
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']

images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

# using matplotlib to plot image and info
for i in range(6):

    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')

    plt.title(titles[i])

plt.xticks([]), plt.yticks([])

plt.show()