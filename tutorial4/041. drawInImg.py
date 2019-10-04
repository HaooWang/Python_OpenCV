#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/4 16:07
# @Author  : HaoWANG
# @Site    : 
# @File    : 041. drawInImg.py
# @Software: PyCharm

# import packages
import cv2 as cv

import numpy as np

# create or read an image
window_name = "Read Image"

# namedWindow and read an image
cv.namedWindow(window_name,cv.WINDOW_NORMAL)
src = cv.imread("../pictures/lena.png")

# drawing lines,circles,rec,eclp, etc.
# cv.line(image, point1,point2, color, weight)
dst1 = cv.line(src,(0,0),(512,512),(100,10,0),10)

# drawing rectangle
dst2 = cv.rectangle(src,(100,100),(200,200),(190,10,105),thickness=10)

# drawing circle
dst = cv.circle(src,(200,200),100,(0,0,255),10)

# drawing ecllips
dst = cv.ellipse(src,(256,256),(100,50),0,0,180,255,5)

pts = np.array([[100,500],[200,300],[100,200],[150,100]], np.int32)

pts = pts.reshape((-1,1,2))

dst3 = cv.polylines(src,[pts],True,(0,255,255))

font = cv.FONT_HERSHEY_SIMPLEX

dst = cv.putText(src,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

# image show
cv.imshow(window_name,dst)


# wait_key operations
cv.waitKey(0)