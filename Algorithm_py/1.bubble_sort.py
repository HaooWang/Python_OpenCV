#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Time   :   2020/10/20 0020  15:11
@Author :   HaoWANG,
@Email  :   haowanghk@163.com
@file   :  1.bubble_sort.py
@Software : Pycharm
@Description:  
"""
import numpy as np
import cv2 as cv

def bubbleSort(array):
    # bubble sort
    arr_len = len(array)
    
    # 遍历数组的所有元素
    for ix in range(arr_len):
        # last index ix elements are always inplace
        for iy in range(arr_len-ix-1):
            if array[iy] > array[iy+1]:
                array[iy], array[iy+1] = array[iy+1], array[iy]
    return array

def main():
    arr = np.arange(10)     #array int [0-9]
    np.random.shuffle(arr)    # 打乱一维数列的顺序，类似于洗牌
    print('排序前数组：{}'.format(arr))
    e1 = cv.getTickCount()      # 计时器e1
    
    arr_sort = bubbleSort(arr)

    e2 = cv.getTickCount()      # 计时器e2
    t = (e2 - e1) / cv.getTickFrequency() # 时间
    print("Time:{}".format(t))
    
    print('排序后数组：{}'.format(arr_sort))
    
if __name__ == "__main__":
    main()
    