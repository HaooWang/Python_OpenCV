#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 17:22
# @Author  : HaoWANG
# @Site    : 
# @File    : python_opencv框架.py
# @Software: PyCharm


#####################################################################

# Example : <................................> processing from a video file
# specified on the command line (e.g. python FILE.py video_file) or from an
# attached web camera
# 视频图像处理流程框架
# 1. 加载包，cv2、numpy、sys等
# 2. 定义并初始化参数
# 3. 定义摄像头捕获类变量cap
# 4. 定义显示窗口
# 5. 常规检测：视频打开成功检测、窗口创建成功检测、文件可读取写入检测等
# 6. 计时并调用OpenCV库函数进行视频帧处理
# 7. 结束计时，将文件写入磁盘，关闭窗口回收资源
#####################################################################
# import packages

import math
import sys

import cv2

#####################################################################
# initialization
keep_processing = True;
camera_to_use = 0;  # 0 if you have one camera, 1 or > 1 otherwise
#####################################################################

# define video capture object
cap = cv2.VideoCapture();

# define display window name
windowName = "Live Camera Input";  # window name
# if command line arguments are provided try to read video_name
# otherwise default to capture from attached H/W camera

if (((len(sys.argv) == 2) and (cap.open(str(sys.argv[1]))))
        or (cap.open(camera_to_use))):

    # create window by name (note flags for resizable or not)
    cv2.namedWindow(windowName, cv2.WINDOW_NORMAL);

    while (keep_processing):
        # error detection #
        # 00 if video file successfully open then read frame from video
        if (cap.isOpened):
            ret, frame = cap.read();
	        
        # start a timer (to see how long processing and display takes)
        start_t = cv2.getTickCount();

        # *******************************

        # *** do any processing here ****

        # *******************************
        frame  = cv2.flip(frame,0)
        # display image
        cv2.imshow(windowName, frame);
        print(frame.shape)
        print(frame.size)
        print(frame.dtype)

        # stop the timer and convert to ms. (to see how long processing and display takes)
        stop_t = ((cv2.getTickCount() - start_t) / cv2.getTickFrequency()) * 1000;
        # wait 40ms or less depending on processing time taken (i.e. 1000ms / 25 fps = 40 ms)

        key = cv2.waitKey(max(2, 40 - int(math.ceil(stop_t)))) & 0xFF;
        # It can also be set to detect specific key strokes by recording which key is pressed
        # e.g. if user presses "x" then exit
        if (key == ord('x')):
            keep_processing = False;

    # close all windows

    cv2.destroyAllWindows()

else:
    print("No video file specified or camera connected.")

#####################################################################
