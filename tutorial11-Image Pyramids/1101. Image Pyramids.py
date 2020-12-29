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
import pathlib

import cv2 as cv
import numpy as np

window_name = "Input Image"
cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)

img_path = "../pictures/dog.jpg"
path = pathlib.Path(img_path)
path.exists()

try:
    img_src = cv.imread(img_path)  # 若能show, 则表示无误；若图片有问题这里会有error
except:
    print(img_path + ' ' + 'have problem!')
    pass
 # img_src = cv.imread(img_path)
# cv.imshow(window_name,img)

lower_reso = cv.pyrDown(img_src)
cv.imshow(window_name,lower_reso)
cv.waitKey(0)
cv.destroyAllWindows()