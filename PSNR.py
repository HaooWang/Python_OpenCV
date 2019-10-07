# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/10/6 20:19
# @Author  : HaoWang
# @Site    : HongKong, China
# @project : $[PROJECT_NAME]
# @File    : PSNR.py
# @Software: PyCharm
# @license: haowanghk@gmail.com 
"""
'''
compute PSNR with tensorflow
'''
import tensorflow as tf


def psnr(tf_img1, tf_img2):
    return tf.image.psnr(tf_img1, tf_img2, max_val=255)
