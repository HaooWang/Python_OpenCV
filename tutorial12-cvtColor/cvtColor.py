#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 12:31
# @Author  : HaoWANG
# @Site    : 
# @File    : cvtColor.py
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
    cap = cv.VideoCapture( )
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
                ret, frame = cap.read( )

            # start a timer (to see how long processing and display takes)
            start_t = cv.getTickCount( )
            # frame = cv.flip(frame, 1)

            # color space transform
            hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

            # upper and lower thresholds
            lower_yel = np.array([26, 43, 46])
            upper_yel = np.array([44, 255, 255])

            mask = cv.inRange(hsv, lower_yel, upper_yel)
            img = cv.bitwise_and(frame, frame, mask = mask)

            # medianBlur 去噪声
            res = cv.medianBlur(src = img, ksize = 5, dst = None)

            # 高斯模糊
            # res = cv.GaussianBlur(img, (7,7), sigmaX= 0.3)

            # canny edge detector
            edges = cv.Canny(res, 50, 150)

            # display image
            cv.imshow(windowName, res)
            # stop the timer and convert to ms. (to see how long processing and display takes)
            stop_t = ((cv.getTickCount( ) - start_t) / cv.getTickFrequency( )) * 1000
            # wait 40ms or less depending on processing time taken (i.e. 1000ms / 25 fps = 40 ms)

            key = cv.waitKey(max(2, 20 - int(math.ceil(stop_t)))) & 0xFF
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


def get_image_info(image):
    print(image.shape[:2])
    print(image.shape)
    print(type(image))
    print(image.size)


print("--------- Information ------")
# mac os
# src = cv.imread("/Users/haowang/ML_CV_Py_worksapce/Python_OpenCV/pictures/coins.jpg")
# windows
# src = cv.imread("E:\Pycharm Projects\Python_opencv3\pictures\coins.jpg")

# cv.namedWindow("Input Image", cv.WINDOW_AUTOSIZE)
# get_image_info(src)
vedio_cap( )
cv.waitKey(0)

# destroy all windows
cv.destroyAllWindows( )
