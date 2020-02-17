# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/10/13 15:01
# @Author  : HaoWang
# @Site    : HongKong, China
# @project : $[PROJECT_NAME]
# @File    : 1101. Image Pyramids.py
# @Software: PyCharm
# @license: haowanghk@gmail.com 
"""

import cv2 as cv
import numpy as np

window_name = "Input Image"
cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)

img = cv.imread("../pictures/dog.jpg")
# cv.imshow(window_name,img)

lower_reso = cv.pyrDown(img)
cv.imshow(window_name,lower_reso)
cv.waitKey(0)
cv.destroyAllWindows()