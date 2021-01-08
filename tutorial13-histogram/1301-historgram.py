#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Copyright:  Jihua Lab 2021.
@File Name   :  1301-historgram.py
@Description:  


@Create Time   :   2021/1/7 0007  15:12
@Author :   HaoWANG, Foshan，China
@Email  :   haowanghk@163.com

@Software : Pycharm
@Version: V1.0

"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def plot_hist_demo(image):
    """
    # 统计并绘制彩色BGR图像灰度值统计直方图
    :param image: src img
    :return:  plt plot
    """
    plt.hist(image.ravel( ), 256, [0, 256])
    plt.show()


def image_hist(image):
    """
    # 彩色图像RGB三通道的灰度直方图绘制
    :param image: 彩色图像
    :return: RGB三通道的灰度直方图
    """
    color = ('blue', 'green', 'red')
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color = color)
        plt.xlim([0, 256])
    plt.show( )

def image_mask_plot(img):
    """
    # 使用make切去ROI区域内的图像统计并绘制直方图
    :param img: color image
    :return: matplotlib plot.show()
    """

    # create a mask
    mask = np.zeros(img.shape[:2], np.uint8)
    mask[50:200, 50:300] = 255
    masked_img = cv.bitwise_and(img, img, mask = mask)
    # Calculate histogram with mask and without mask
    # Check third argument for mask
    hist_full = cv.calcHist([img], [0], None, [256], [0, 256])
    hist_mask = cv.calcHist([img], [0], mask, [256], [0, 256])

    # cvt color space from OpenCV BGR to RGB
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    mask = cv.cvtColor(mask, cv.COLOR_BGR2RGB)
    masked_img  = cv.cvtColor(masked_img, cv.COLOR_BGR2RGB)

    # matplotlib subplot src images and their histogram
    plt.subplot(221), plt.imshow(img, 'gray')
    plt.subplot(222), plt.imshow(mask, 'gray')
    plt.subplot(223), plt.imshow(masked_img, 'gray')
    plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
    plt.xlim([0, 256])
    plt.show( )

def main():
    print("---------Histogram Plot Python ---------")
    src = cv.imread("../pictures/cat.jpg")
    cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
    cv.imshow("input image", src)
    # gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY) # color cvt BGR->gray
    # plot_hist_demo(gray)  # plot the source image histgram
    image_hist(src)
    # image_mask_plot(src) # Application of Mask
    cv.waitKey(0)
    cv.destroyAllWindows( )  # destroy all windows


if __name__ == '__main__':
    main( )
