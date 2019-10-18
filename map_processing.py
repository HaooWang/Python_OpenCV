#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 2:13 PM
# @Author  : HaoWang
# @Site    : 
# @File    : map_processing.py
# @Software: PyCharm

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


class Map2Binary:
    def __init__(self):
        pass


def rgb_map2_binary_map(src_bgr,
                        thres):
    # 将原图像拷贝为灰度图，并进行高斯模糊、阈值分割、形态学操作和二值化操作
    # 形参表：src_bgr thres (value 0 - 255)
    src_gray = cv.cvtColor(src_bgr, cv.COLOR_BGR2GRAY)

    ret2, th2 = cv.threshold(src_gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    return th2


def main():
    # main 函数完成图像image或者frame视频帧读取和预处理

    kernel = np.ones((13, 13), np.uint8)
    kernel_c = np.ones((19, 19), np.uint8)

    src = cv.imread("/Users/haowang/AI/Python_OpenCV/pictures/GradMap.jpg")

    src_opening = cv.morphologyEx(src, cv.MORPH_OPEN, kernel)  # 开运算去除噪声和道路特征点

    src_blur = cv.GaussianBlur(src_opening, (9, 9), 0)  # 高斯模糊

    src_closing = cv.morphologyEx(src_blur, cv.MORPH_CLOSE, kernel_c)  # 闭运算将离散的点边界连接

    map_gray = cv.cvtColor(src_closing, cv.COLOR_BGR2GRAY)   # 灰度图

    ret1, th1 = cv.threshold(map_gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)  #OTUS阈值分割

    bina_map = cv.bitwise_not(th1)
    # bina_map = cv.cvtColor(bina_map, cv.COLOR_GRAY2RGB)

    dst = cv.medianBlur(bina_map, 11)

    plt.subplot(131), plt.imshow(src), plt.title("Input Map Image")
    plt.subplot(132), plt.imshow(src_opening), plt.title("Processed Open Image")
    plt.subplot(133), plt.imshow(src_closing), plt.title("Processed Closing Image")
    plt.subplot(231), plt.imshow(map_gray), plt.title("Input Gray Map Image")
    plt.subplot(232), plt.imshow(dst), plt.title("Processed Threshold Image : thred" + str(ret1))
    plt.subplot(233), plt.imshow(bina_map), plt.title("Processed Binary Image")
    plt.xticks([]), plt.yticks([])

    plt.show()


if __name__ == "__main__":
    main()
