# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/10/30 18:14
# @Author  : HaoWang
# @Site    : HongKong, China
# @project : $[PROJECT_NAME]
# @File    : 1202Image.py
# @Software: PyCharm
# @license: haowanghk@gmail.com 
"""

import numpy as np
import cv2

im = cv2.imread('pictures/rice.png')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print("contours:",np.shape(contours))
# (579,)
# draw contours
cont_img = cv2.drawContours(im, contours, -1, (0,255,0), 3)


# 计算图像的距
cnt = contours[0]
M = cv2.moments(cnt)
print(M)

# # 计算对象重心
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

# 计算面积
area = cv2.contourArea(cnt)
print(area)

# 计算周长
perimeter = cv2.arcLength(cnt,True)

# 轮廓近似
epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)

# 凸包
# hull = cv2.convexHull(points[, hull[, clockwise[, returnPoints]]
hull = cv2.convexHull(cnt, returnPoints=False)

# 凸性检验
k = cv2.isContourConvex(cnt)
print(k)

# 边界矩形(正)
x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)

# 边界矩形+旋转
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img,[box],0,(0,0,255),2)

# 最小外接圆
(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
img = cv2.circle(img,center,radius,(0,255,0),2)

# 椭圆拟合
ellipse = cv2.fitEllipse(cnt)
im = cv2.ellipse(im,ellipse,(255,0,0),2)

# 直线拟合
rows,cols = img.shape[:2]
#cv2.fitLine(points, distType, param, reps, aeps[, line ]) → line
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
img = cv2.line(img,(cols-1,righty),(0,lefty),(255,255,0),2)

# plot image
cv2.imshow("Contour Image Info: "+
           "area:"+ str(area) +
           "/length : %.2f "%perimeter +
          " Convex: "+str(k),
           img)

# print(hull)
# print(cnt[69])

# wait
cv2.waitKey(0)
cv2.destroyAllWindows()

