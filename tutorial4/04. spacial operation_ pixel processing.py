#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 13:53
# @Author  : HaoWANG
# @Site    : 
# @File    : 04. spacial operation_ pixel processing.py
# @Software: PyCharm


import math
import sys

import numpy as np
import cv2 as cv


def vedio_cap():
    # initialization
    keep_processing = True
    camera_to_use = 0  # 0 if you have one camera, 1 or > 1 otherwise
    # define video capture object
    cap = cv.VideoCapture()
    # define display window name
    windowName = "Live Camera Input"
    # if command line arguments are provided try to read video_name
    # otherwise default to capture from attached H/W camera

    if (((len(sys.argv) == 2) and (cap.open(str(sys.argv[1]))))
            or (cap.open(camera_to_use))):

        # create window by name (note flags for resizable or not)
        cv.namedWindow(windowName, cv.WINDOW_NORMAL)
        while (keep_processing):
            # error detection #
            if (cap.isOpened):
                ret, frame = cap.read()

            # start a timer (to see how long processing and display takes)
            start_t = cv.getTickCount()
            frame = cv.flip(frame, 1)
            # display image
            cv.imshow(windowName, frame)
            # stop the timer and convert to ms. (to see how long processing and display takes)
            stop_t = ((cv.getTickCount() - start_t) / cv.getTickFrequency()) * 1000
            # wait 40ms or less depending on processing time taken (i.e. 1000ms / 25 fps = 40 ms)

            key = cv.waitKey(max(2, 40 - int(math.ceil(stop_t)))) & 0xFF
            # It can also be set to detect specific key strokes by recording which key is pressed
            # e.g. if user presses "x" then exit
            if (key == ord('x')):
                keep_processing = False
                print("frame shape: {}. ".format(frame.shape))
                gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                cv.imwrite("E:/Pycharm Projects/Python_OpenCV/pictures/frameGRAY.png", gray)
                print("-- key == ord('x') --")

        # close all windows
        cv.destroyWindow(windowName)


def add_image(img1, img2):
    dst = cv.add(img1, img2)
    cv.imshow("Add image", dst)


def subtract_image(img1, img2):
    dst = cv.subtract(img1, img2)
    cv.imshow("Subtract image", dst)


def mean_img(img1, img2):
    # N1 = np.array([])
    # N2 = np.array([])
    N1 = cv.mean(img1)
    N2 = cv.mean(img2)
    print(N1, "\t", N2)

def logic_operation(img1,img2):
    dst = cv.bitwise_and(img1,img2) # and
    #dst = cv.bitwise_not()
    #dst =cv.bitwise_or()
    #dst = cv.bitwise_xor()

    return dst

def contrast_brightness(img, c, b):
    h, w, ch = img.shape
    blank = np.zeros([h,w,ch], img.dtype)
    dst = cv.addWeighted(img,c,blank,1-c,b)
    cv.imshow("con-bri",dst)

def get_image_info(image):
    print(image.shape)
    print(type(image))
    print(image.size)


print("--------- Information ------")
src1 = cv.imread("/Users/haowang/Desktop/image_dataset/misc/4.1.05.tiff")
src2 = cv.imread("/Users/haowang/Desktop/image_dataset/misc/4.1.07.tiff")
cv.namedWindow("Input Image 1", cv.WINDOW_NORMAL)
cv.namedWindow("Input Image 2", cv.WINDOW_NORMAL)
cv.imshow("Input Image 1", src1)
cv.imshow("Input Image 2", src2)
cv.imshow("AND",logic_operation(src1,src2))

add_image(src1, src2)
subtract_image(src1, src2)
mean_img(src1, src2)
contrast_brightness(src1,1.2,10)
get_image_info(src1)
get_image_info(src2)

cv.waitKey(0)

# destroy all windows
cv.destroyAllWindows()
