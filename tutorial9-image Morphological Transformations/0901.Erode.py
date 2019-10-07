# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/10/7 10:56
# @Author  : HaoWang
# @Site    : HongKong, China
# @project : $[PROJECT_NAME]
# @File    : 0901.Erode.py
# @Software: PyCharm
# @license: haowanghk@gmail.com
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


src = cv.imread("../pictures/binary.png",0)

# erosion
kernel = np.ones((5,5), np.uint8)
erosion = cv.erode(src=src,kernel=kernel, iterations=1)

# dilation
dilation = cv.dilate(src, kernel,iterations =1 )

plt.subplot(131),plt.imshow(src),plt.title("Original Image : "+ str(np.shape(src)))
plt.subplot(132),plt.imshow(erosion), plt.title("Erosion Image " )
plt.subplot(133), plt.imshow(dilation), plt.title("Dilation Image " )

plt.show()