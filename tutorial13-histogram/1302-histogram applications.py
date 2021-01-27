#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Copyright:  Jihua Lab 2021.
@File Name   :  1302-histogram applications.py
@Description:  彩色图、灰度图直方图统计、直方图绘制、直方图均衡化、直方图对比。


@Create Time   :   2021/1/8 0008  8:57
@Author :   HaoWANG, Foshan，China
@Email  :   haowanghk@163.com

@Software : Pycharm
@Version: V1.3

"""

import os

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def equal_hist_demo(image):
    """
    直方图均衡化操作
    :param image: 输入为三通道彩色图像
    :return: 显示直方图均衡化结果
    """
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    res = np.hstack((gray, dst))  # stacking images side-by-side
    print("--------Histogram equalization and plot  --------")
    cv.imshow("stacking images side-by-side", res)
    cv.imshow("equalization result", dst)
    cv.imwrite("../pictures/equ_lena.png", dst)

    # plot histogram equalization result
    hist, bins = np.histogram(gray.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * float(hist.max()) / cdf.max()
    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    # cdf = np.ma.filled(cdf_m, 0).astype('uint8')

    plt.plot(cdf_m, color = 'k')  # plot cdf mask
    plt.plot(cdf_normalized, color = 'b')  # plot normalized cdf

    plt.hist(gray.flatten(), 256, [0, 256], color = 'r')  # src gray image hist
    plt.hist(dst.flatten(), 256, [0, 256], color = 'y')  # dst equalized gray image hist

    plt.xlim([0, 256])
    plt.legend(('cdf_m', 'cdf_normalized', 'src histogram', "equalized hist"), loc = 'upper left')
    plt.show()


def clahe_demo(image):
    """
    克拉赫(Contrast Limited 适应直方图均衡化)
    :param image: 三通道彩色图像
    :return:绘制均衡化之后的结果图像
    """

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # 彩色图像灰度化
    clahe = cv.createCLAHE(clipLimit = 1.0, tileGridSize = (8, 8))
    """
     @brief Creates a smart pointer to a cv::CLAHE class and initializes it.
    .   
    .   @param clipLimit Threshold for contrast limiting.
    .   @param tileGridSize Size of grid for histogram equalization. Input image will be divided into
    .   equally sized rectangular tiles. tileGridSize defines the number of tiles in row and column.
    """
    dst = clahe.apply(gray)
    print("--------Histogram equalization clahe_demo --------")

    # plot histogram equalization result
    hist, bins = np.histogram(gray.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * float(hist.max()) / cdf.max()
    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    # cdf = np.ma.filled(cdf_m, 0).astype('uint8')

    plt.plot(cdf_m, color = 'k')  # plot cdf mask
    plt.plot(cdf_normalized, color = 'b')  # plot normalized cdf

    plt.hist(gray.flatten(), 256, [0, 256], color = 'r')  # src gray image hist
    plt.hist(dst.flatten(), 256, [0, 256], color = 'y')  # dst equalized gray image hist

    plt.xlim([0, 256])
    plt.legend(('cdf_m', 'cdf_normalized', 'src histogram', "equalized hist"), loc = 'upper left')
    plt.show()
    cv.imshow("clahe_demo", dst)
    cv.imwrite("../pictures/clahe_lena.png", dst)


def create_rgb_hist(image):
    """
    :param image:
    :return:
    """
    h, w, c = image.shape
    rgb_hist = np.zeros([16 * 16 * 16, 1], np.float32)
    bsize = 256 / 16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = np.int(b / bsize) * 16 * 16 + np.int(g / bsize) * 16 + np.int(r / bsize)
            rgb_hist[np.int(index), 0] = rgb_hist[np.int(index), 0] + 1
    return rgb_hist


def hist_compare(image1, image2):
    """

    :param image1:
    :param image2:
    :return:
    """
    hist1 = create_rgb_hist(image1)
    hist2 = create_rgb_hist(image2)
    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print("巴氏距离: %s, 相关性: %s, 卡方: %s" % (match1, match2, match3))


def main():
    """
    主调函数
    :return:
    """

    img_path = "../pictures/lena-noisy.png"  # input image path

    # 检查图像读取路径合法性
    if not (os.path.exists(img_path) and
            os.access(img_path, os.R_OK)):
        # 判断文件路径是否存在; 检查文件是否可读
        print(img_path + ' ' + 'have problem!')
        print("ERROR : File is not exists or un-accessible to read")
    else:
        print("--------------------------")
        print("File is accessible to read")
        print("---------Histogram Plot Python ---------")
        window_name = "Input Image"
        cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)
        image_lena = cv.imread(img_path)

        # image blur
        # dst = cv.medianBlur(image_lena,3)
        dst = cv.GaussianBlur(image_lena, (5, 5), sigmaX = 1.1)

        cv.imshow(window_name, image_lena)
        cv.imshow("GaussianBlur", dst)

        # histogram comp
        image1 = cv.imread("../pictures/lena.png")
        image2 = cv.imread("../pictures/lenanoise.png")

        #######
        # hist_compare(image1, image2)
        #######

        #######
        # clahe_demo(image_lena)
        #######

        #######
        # equalHist_demo(image_lena)
        #######

        cv.waitKey(0)
        cv.destroyAllWindows()  # destroy all windows


if __name__ == '__main__':
    main()
