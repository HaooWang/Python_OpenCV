#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 13:32
# @Author  : HaoWANG
# @Site    : 
# @File    : 02.Numpy array operations.py
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


######
# access each pixel

def access_pixels(image):
	print(image.shape)
	height = image.shape[0]
	width = image.shape[1]
	channels = image.shape[2]
	print("width: %s, height: %s, channels: %s" % (width, height, channels))
	for row in range(width):
		for col in range(height):
			for channel in range(channels):
				pix = image[row, col, channel]
				image[row, col, channel] = 255 - pix
	cv.imwrite("/Users/haowang/AI/Python_OpenCV/pictures/lena.png", image)
	cv.imshow("access_pixels", image)


#########################################################
# using numpy array to access image pixels

def creat_image(image):
	img = np.zeros([512, 512, 3], np.uint8)
	img = image
	img[:, :, 1] = np.ones([512, 512]) + 100
	cv.imshow("new iamge", img)


# Inverse API

def inverse(image):
	dst = cv.bitwise_not(image)
	cv.imshow("inverse demo", dst)


print("-----Image Information")
src = cv.imread("/Users/haowang/AI/Python_OpenCV/pictures/lena.png")  # B + G + R = 3 channels
cv.namedWindow("Input Image", cv.WINDOW_AUTOSIZE)
cv.imshow("Input Image", src)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imwrite("E:/Pycharm Projects/Python_OpenCV/pictures/grayLena.png", gray)
t1 = cv.getTickCount()
inverse(src)
t2 = cv.getTickCount()
time = (t2 - t1) / cv.getTickFrequency() * 1000
print("access_pixels time is : {} ms".format(time))
cv.waitKey(0)

cv.destroyWindow()
