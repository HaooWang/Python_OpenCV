#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/2 16:07
# @Author  : HaoWANG
# @Site    : 
# @File    : multiThreaded_video.py
# @Software: PyCharm
#!/usr/bin/env python3

'''
Multithreaded video processing minimal sample.
Usage:
   python3 video_threaded.py
   Shows how python threading capabilities can be used
   to organize parallel captured frame processing pipeline
   for smoother playback.
Keyboard shortcuts:
   ESC - exit
'''
from collections import deque
from multiprocessing.pool import ThreadPool

import cv2 as cv
import numpy as np
import time

VIDEO_SOURCE = 0

# 创建对象
# 对于SIFT算子，可以通过nFeatures属性控制特征点数量
SIFT = cv.xfeatures2d_SIFT.create()


def process_frame1(frame):
    # some intensive computation...
    # frame = cv.medianBlur(frame, 19)
    flip_fra = cv.flip(frame,-1)
    mean_filter_image = cv.bilateralFilter(flip_fra,d=5,sigmaColor=10,sigmaSpace=10)
    return mean_filter_image



 # some intensive computation...
#  SIFT Feature extraction via opencv- python
def process_frame(src):
    frame = cv.flip(src,-1) # flip the video frame
    # 新建一个空图像用于绘制特征点
    img_sift = np.zeros(src.shape, np.uint8)
    # 提取特征并计算描述子
    kps, des = cv.xfeatures2d_SIFT.detectAndCompute(SIFT, frame, None)
    cv.drawKeypoints(frame, kps, img_sift)
    return img_sift


if __name__ == '__main__':
    # Setup.
    cap = cv.VideoCapture(VIDEO_SOURCE)
    thread_num = cv.getNumberOfCPUs()
    pool = ThreadPool(processes=thread_num)
    pending_task = deque()

    while True:
        #1. FPS counting
        # Start time
        start = time.time()
        
        # 2. Consume the queue.
        while len(pending_task) > 0 and pending_task[0].ready():
            res = pending_task.popleft().get()
            cv.imshow('threaded video', res)

        # 3. Populate the queue.
        if len(pending_task) < thread_num:
            frame_got, frame = cap.read()
            if frame_got:
                task = pool.apply_async(process_frame, (frame.copy(),))
                pending_task.append(task)
                
        # End time
        end = time.time()
        # Time elapsed
        seconds = end - start
        # print("Time taken : {0} seconds".format(seconds))
        # Calculate frames per second
        fps = 1 / seconds
        print("Estimated frames per second : {0}".format(fps))
        
        
        # Write FPS on live video
        # text = "FPS:" + str(fps)
        # cv.putText(res, text, (40, 50), cv.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 255), 2)
        #
        # 5. Show preview.
        if cv.waitKey(1) == 27 or not frame_got:
            break

cv.destroyAllWindows()