#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 14:33
# @Author  : HaoWANG
# @Site    : 
# @File    : 03.color space.py
# @Software: PyCharm
import math
import sys

import cv2 as cv
import numpy as np


# get image or video information
def get_image_info(image):
	print('image.shape:', image.shape)
	print('image type:', type(image))
	print('image size:', image.size)


###################
# image color space transformation

def color_space(image):
	gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
	cv.imshow("RGB To Gray", gray)
	hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
	cv.imshow("RGB To HSV", hsv)
	yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
	cv.imshow("YUV", yuv)
	ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
	cv.imshow("YCrCb", ycrcb)


# native feature extraction
def feature_extraction(image):
	hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
	lower_hsv = np.array([0, 0, 0])
	upper_hsv = np.array([180, 255, 46])
	mask = cv.inRange(image, lowerb=lower_hsv, upperb=upper_hsv)
	return mask


def vedio_cap():
	# initialization
	keep_processing = True
	camera_to_use = 0  # 0 if you have one camera, 1 or > 1 otherwise
	# define video capture object
	cap = cv.VideoCapture()
	# define display window name
	windowNameInit = "Live Camera Input"
	windowNameProc = "Processed Camera Vedio"
	# if command line arguments are provided try to read video_name
	# otherwise default to capture from attached H/W camera
	
	if (((len(sys.argv) == 2) and (cap.open(str(sys.argv[1]))))
			or (cap.open(camera_to_use))):
		
		# create window by name (note flags for resizable or not)
		cv.namedWindow(windowNameInit, cv.WINDOW_NORMAL)
		cv.namedWindow(windowNameProc, cv.WINDOW_NORMAL)
		
		while (keep_processing):
			# error detection #
			if (cap.isOpened):
				ret, frame = cap.read()
			
			# start a timer (to see how long processing and display takes)
			start_t = cv.getTickCount()
			flip_frame = cv.flip(frame, -1)
			mask = feature_extraction(flip_frame)
			
			# display vedio
			cv.imshow(windowNameInit, flip_frame)
			cv.imshow(windowNameProc, mask)
			# stop the timer and convert to ms. (to see how long processing and display takes)
			stop_t = ((cv.getTickCount() - start_t) / cv.getTickFrequency()) * 1000
			# wait 40ms or less depending on processing time taken (i.e. 1000ms / 25 fps = 40 ms)
			
			key = cv.waitKey(max(2, 40 - int(math.ceil(stop_t)))) & 0xFF
			# It can also be set to detect specific key strokes by recording which key is pressed
			# e.g. if user presses "x" then exit
			if (key == ord('x')):
				keep_processing = False
				print("frame shape: {}. ".format(flip_frame.shape))
				gray = cv.cvtColor(flip_frame, cv.COLOR_BGR2GRAY)
				cv.imwrite("E:/Pycharm Projects/Python_OpenCV/pictures/frameGRAY.png", gray)
				print("-- key == ord('x') --")
		
		# close all windows
		cv.destroyWindow(windowNameInit)
		cv.destroyWindow(windowNameProc)


print("--------- Information ------")
# initial tick counter t1
t1 = cv.getTickCount()
# processing
vedio_cap()

# tick counter t2
t2 = cv.getTickCount()
time = (t2 - t1) / cv.getTickFrequency() * 1000

print("Time consumption during this process : {} ms.".format(time))
cv.waitKey(0)

# destroy all windows
cv.destroyAllWindows()
