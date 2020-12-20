#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 11:26
# @Author  : HaoWANG
# @Site    : 
# @File    : trackbar_create and pos.py
# @Software: PyCharm

import cv2 as cv
import sys
import math


# Living Vedio Image Capture
def vedio_cap():
	# initialization
	keep_processing = True
	camera_to_use = 0  # 0 if you have one camera, 1 or > 1 otherwise
	# define video capture object
	cap = cv.VideoCapture()
	# define display window name
	windowName = "image"
	# if command line arguments are provided try to read video_name
	# otherwise default to capture from attached H/W camera
	
	if (((len(sys.argv) == 2) and (cap.open(str(sys.argv[1]))))
			or (cap.open(camera_to_use))):
		
		# create window by name (note flags for resizable or not)
		cv.namedWindow(windowName, cv.WINDOW_NORMAL)
		# create track bar window in image show Window
		cv.createTrackbar('R', 'image', 0, 255, callBack)
		cv.createTrackbar('G', 'image', 0, 255, callBack)
		cv.createTrackbar('B', 'image', 0, 255, callBack)
		switch = '0:OFF\n1:ON'
		cv.createTrackbar(switch, 'image', 0, 1,callBack)
		
		while (keep_processing):
			# error detection #
			if (cap.isOpened):
				ret, frame = cap.read()
			
			r = cv.getTrackbarPos('R', 'image')
			g = cv.getTrackbarPos('G', 'image')
			b = cv.getTrackbarPos('B', 'image')
			s = cv.getTrackbarPos(switch, 'image')
			if s == 0:
				frame[:] = 0
			else:
				frame[:] = [b, g, r]
			
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
		
# call back function of creattrackbar()
def callBack():
	pass

# main function
def main():
	vedio_cap()


if __name__ == '__main__':
    main()

		

