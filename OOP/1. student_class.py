#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Copyright:  Jihua Lab 2021.
@File Name   :  1. student_class.py
@Description:  


@Create Time   :   2021/1/27 0027  9:06
@Author :   HaoWANG, Foshan，China
@Email  :   haowanghk@163.com

@Software : Pycharm
@Version: V1.0

"""


class Student(object):
    # Student 类
    # 成员函数：

    def __init__(self, name, score):
        '''
        :param name: 初始化类对象，self、name、score
        :param score:
        '''
        if (score >= 0 and score <= 100):
            self.__score = score
            if isinstance(name, str):
                self.__name = name
                print("----object {} is Initialised --- ".format(self.__name))
            else:
                raise ValueError('bad name string')
        else:
            print("ERROR: score>=0 and score <=100 ?")

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        self.__score = new_score
        return True

    def get_grade(self):
        '''
        :return: student对象分数等级 A、B、C
        '''
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def print_info(self):
        print("----Student {} info printing----".format(self.__name))
        print("{} info {}".format(self.__name, dir(self)))
        print("Name: {}     Score: {}    Grade: {}  "
              .format(self.__name, self.__score, self.get_grade()))


def main():
    student_list = []
    lisa = Student('lisa', 93)  # 声明类对象lisa并初始化该对象
    student_list.append(lisa)
    bear = Student('bear', 75)  # 声明类对象bear并初始化该对象
    student_list.append(bear)
    lisa.print_info()  # 打印类对象信息
    if (bear.set_score(new_score=100) == True):
        print('--set score: {} Success!--'.format(bear.get_score()))
    bear.print_info()
    for item in student_list:  # 存放类对象的内存空间
        print(item)


if __name__ == '__main__':
    main()
