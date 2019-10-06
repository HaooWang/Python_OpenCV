#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/5 3:57 PM
# @Author  : HaoWang
# @Site    : 
# @File    : 033.Affin Transformation.py
# @Software: PyCharm

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('../pictures/lena.png')

rows,cols,ch = img.shape # color image

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv.getAffineTransform(pts1,pts2)
dst = cv.warpAffine(img,M,(cols,rows))

RGB_img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
RGB_dst = cv.cvtColor(dst,cv.COLOR_BGR2RGB)

plt.subplot(121),plt.imshow(RGB_img),plt.title('Input')
plt.subplot(122),plt.imshow(RGB_dst),plt.title('Output')
plt.show()

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()