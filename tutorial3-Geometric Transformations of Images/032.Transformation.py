#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/5 3:29 PM
# @Author  : HaoWang
# @Site    : 
# @File    : 032.Transformation.py
# @Software: PyCharm

import numpy as np
import cv2 as cv
img = cv.imread('../pictures/lena.png',0)
rows,cols = img.shape
M = np.float32([[1,0,100],[0,1,50]])
dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()