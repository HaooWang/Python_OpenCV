#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/5 2:20 PM
# @Author  : HaoWang
# @Site    : 
# @File    : 061.addNoise.py
# @Software: PyCharm


# Parameters
# ----------
# image : ndarray
#     Input image data. Will be converted to float.
# mode : str
#     One of the following strings, selecting the type of noise to add:
#
#     'gauss'     Gaussian-distributed additive noise.
#     'poisson'   Poisson-distributed noise generated from the data.
#     's&p'       Replaces random pixels with 0 or 1.
#     'speckle'   Multiplicative noise using out = image + n*image,where
#                 n is uniform noise with specified mean & variance.
# prob: float number
#      probability between 0 and 1, mainly around 0.1
# var and mean: noise mean, generally gaussian niose with 0 mean and var


import numpy as np
import cv2 as cv
from PSNR import psnr
# import sys
# import random


def noisy(noise_typ, image, var=0.1, mean=0):
    #  Add Gaussian noise
    if noise_typ == "gauss":
        row, col, ch = image.shape
        sigma = var ** 0.5
        gauss = np.random.normal(mean, sigma, (row, col, ch))
        gauss = gauss.reshape(row, col, ch)
        noisy = image + gauss
        return noisy

    # Add Salt and Pepper noise
    elif noise_typ == "s&p":
        row, col, ch = image.shape
        s_vs_p = 0.5
        amount = 0.004
        out = np.copy(image)
        # Salt mode
        num_salt = np.ceil(amount * image.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt))
                  for i in image.shape]
        out[coords] = 1

        # Pepper mode
        num_pepper = np.ceil(amount * image.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper))
                  for i in image.shape]
        out[coords] = 0
        return out

    # Add Poisson noise
    elif noise_typ == "poisson":
        vals = len(np.unique(image))
        vals = 2 ** np.ceil(np.log2(vals))
        noisy = np.random.poisson(image * vals) / float(vals)
        return noisy

    # Add Speckle noise
    elif noise_typ == "speckle":
        row, col, ch = image.shape
        gauss = np.random.randn(row, col, ch)
        gauss = gauss.reshape(row, col, ch)
        noisy = image + image * gauss
        return noisy


def main():

    src = cv.imread("../pictures/lena.png")
    # if(not src ):
    #     print("IMAGE READE ERROR:imread: ../pictures/lena.png")
    #     return 0

    # define a GUI Window
    window_name = "Input Image"
    cv.namedWindow(window_name,cv.WINDOW_AUTOSIZE)
    cv.imshow(window_name,src)

#     add gaussian noise
    noisy_image = noisy("s&p",src)
    # define a GUI Window

    cv.namedWindow("Noisy Image",cv.WINDOW_AUTOSIZE)
    cv.imshow("Noisy Image",noisy_image)
    
    print("psnr(src, noisy_image): ",
          psnr(src, noisy_image))
    cv.waitKey(0)
    
    # destroy all windows
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
