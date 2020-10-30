#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 13:55
# @Author  : HaoWANG
# @Site    : 
# @File    : 05.ROI.py
# @Software: PyCharm


import math
import sys

import cv2 as cv
import numpy as np

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


def get_image_info(image):
    print(image.shape)
    print(type(image))
    print(image.size)

def file_color(img):
    copyImg = img.copy()
    h, w =img.shape[:2]
    mask = np.zeros([h+2, w+2], np.uint8)
    cv.floodFill(copyImg,mask,(30,30),(0,255,255),(100,100,100),(50,50,50),cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("File_color", copyImg)

def fill_binary():
    image = np.zeros([200,200,3],np.uint8)
    image[100:200,100:200,:] =255
    cv.imshow("Img",image)

    mask = np.ones([202,202,1], np.uint8)
    mask[101:201,101:201] = 0
    cv.floodFill(image, mask,(150,100),(0,0,255),cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("T",image)

print("--------- Information ------")
src = cv.imread("/Users/haowang/Desktop/image_dataset/misc/4.1.04.tiff")
cv.namedWindow("Input Image", cv.WINDOW_NORMAL)
cv.imshow("Input Image", src)

get_image_info(src)

roi = src[40:180, 100:210]   # （height，wide）---行起始位置60：180，列起始位置100：200
cv.imshow("ROI", roi)

roi_gray = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
back = cv.cvtColor(roi_gray, cv.COLOR_GRAY2BGR)
src[40:180, 100:210] = back
cv.imshow("GRAY", src)
#file_color(src)
fill_binary()
cv.waitKey(0)

# destroy all windows
cv.destroyAllWindows()
