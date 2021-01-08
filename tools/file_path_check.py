#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Time   :   2020/12/29 0029  8:50
@Author :   HaoWANG,
@Email  :   haowanghk@163.com
@file   :
@Software : Pycharm
@Description:
"""

import os
import pathlib
import cv2 as cv
import numpy as np

img_path = "../pictures/dog.jpg"

#

# 方法1 ： (推荐) try直接使用open()方法来检查文件是否存在和可读写。
# try:
#     img_file = open(img_path)  # 若能open, 则表示无误；若图片有问题这里会有error
#     img_file.close()
#     img_src = cv.imread(img_path)
#
# except IOError:
#     print(img_path + ' ' + 'have problem!')
#     pass

# 方法2： 使用pathlib模块
# 检查路径是否存在

# path = pathlib.Path(img_path)
# path.exists()
#
# if path.exists() is True:
#     img_src = cv.imread(img_path)

# 方法3： 推荐-使用os模块
# os模块中的os.path.exists()方法用于检验文件是否存在。

if not (os.path.exists(img_path) and
        os.access(img_path, os.R_OK)):
    # 判断文件路径是否存在; 检查文件是否可读
    print(img_path + ' ' + 'have problem!')
    print("ERROR : File is not exists or un-accessible to read")
else:
    print("--------------------------")
    print("File is accessible to read")
    window_name = "Input Image"
    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)
    img_src = cv.imread(img_path)
    lower_reso = cv.pyrDown(img_src)
    cv.imshow(window_name, lower_reso)
    cv.waitKey(0)
    cv.destroyAllWindows( )
