#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 14:52
# @Author  : HaoWANG
# @Site    : 
# @File    : 1003. CannyEdges.py
# @Software: PyCharm

import numpy as np
import cv2 as cv

from matplotlib import pyplot as plt


img = cv.imread('../pictures/google.png',0)

# canny edge detector
edges = cv.Canny(img,50,150)

# show images
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

# plt.show()
plt.show()