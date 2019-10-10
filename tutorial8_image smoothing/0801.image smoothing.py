# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/10/6 17:18
# @Author  : HaoWang
# @Site    : HongKong, China
# @project : $[PROJECT_NAME]
# @File    : 0801.image filter2d.py
# @Software: PyCharm
# @license: haowanghk@gmail.com 
"""

import numpy as np
import cv2 as cv
import tensorflow as tf
from PSNR import psnr
from matplotlib import pyplot as plt




# read noisy image
img = cv.imread('../pictures/room.jpg')

# define filter kernel
kernel = np.ones((7,7),np.float32)/25

dst_2d = cv.filter2D(img,-1,kernel)

dst_g = cv.GaussianBlur(img,(7,7),0)

# .   cv.boxFilter(src, ddepth, ksize)
#         @param src input image.
#     .   @param dst output image of the same size and type as src.
#     .   @param ddepth the output image depth (-1 to use src.depth()).
#     .   @param ksize blurring kernel size.
dst_box = cv.boxFilter(img, -1, (5,5))

# bilateral filter
dst_bilateral = cv.bilateralFilter(img,16,75,75)

# median filter
dst_m = cv.medianBlur(img,5)

# change color space fromBGR to RGB
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
dst_g = cv.cvtColor(dst_g,cv.COLOR_BGR2RGB)
dst_2d = cv.cvtColor(dst_2d,cv.COLOR_BGR2RGB)
dst_box = cv.cvtColor(dst_box,cv.COLOR_BGR2RGB)
dst_bilateral = cv.cvtColor(dst_bilateral, cv.COLOR_BGR2RGB)
dst_m = cv.cvtColor(dst_m, cv.COLOR_BGR2RGB)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    PSNR_2d = sess.run(psnr(img, dst_2d))
    PSNR_bil = sess.run(psnr(img, dst_bilateral))
    PSNR_Gua = sess.run(psnr(img, dst_g))
    PSNR_m = sess.run(psnr(img,dst_m))

# plt.subplot(111),plt.imshow(img),plt.title('Original')
#
# plt.xticks([]), plt.yticks([])

# plt.subplot(111),plt.imshow(dst_bilateral),plt.title('Bilateral Filter & PSNR:'+str(PSNR_bil))
#
# plt.xticks([]), plt.yticks([])

# plt.subplot(111),plt.imshow(dst_g),plt.title("Gaussian " + str(np.shape(kernel))+ "PSNR : " +str(PSNR_Gua))
#
# plt.xticks([]), plt.yticks([])

# plt.subplot(121),plt.imshow(dst_2d),plt.title("2dFilter " + str(np.shape(kernel))+ "PSNR : " +str(PSNR_2d))
#
# plt.xticks([]), plt.yticks([])

plt.subplot(111),plt.imshow(dst_m),plt.title("medianFilter " + "PSNR : " +str(PSNR_m))

plt.xticks([]), plt.yticks([])

plt.show()


