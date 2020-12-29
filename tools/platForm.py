#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Time   :   2020/10/30 0030  14:23
@Author :   HaoWANG,
@Email  :   haowanghk@163.com
@file   :  platForm.py
@Software : Pycharm
@Description:  
"""
import os
import platform


def img_path():
    if platform.system() == "Linux":
        if os.path.exists("/root/"):
            pass
        else:
            os.makedirs("/root/")
        return "/root/"
    elif platform.system() == "Windows":
        if os.path.exists("E:/Pycharm Projects"):
            print("Workspace Path in Windows is : {}".format(os.path.abspath('..')))
            return os.path.abspath('..')
        else:
            os.makedirs("Workspace Path in Windows E:/Pycharm Projects is not exists.")
    exit()
def main():
    img_path()
    
if __name__ == '__main__':
    main()