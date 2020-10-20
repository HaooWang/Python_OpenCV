#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 12:42
# @Author  : HaoWANG
# @Site    : 
# @File    : bgr_hsv_tools.py
# @Software: PyCharm

import cv2
import numpy as np

yellow =np.uint8([[[0, 255, 255]]])
hsv_yellow=cv2.cvtColor(yellow, cv2.COLOR_BGR2HSV)
print("hsv_green:", hsv_yellow)