#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Copyright:  Jihua Lab 2021.
@File Name   :  1303-histogram equalization.py
@Description:  


@Create Time   :   2021/1/8 0008  9:07
@Author :   HaoWANG, Foshan，China
@Email  :   haowanghk@163.com

@Software : Pycharm
@Version: V1.0

"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('../pictures/lenanoise.png',0)
hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()