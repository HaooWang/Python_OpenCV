#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Copyright:  Jihua Lab 2021.
@File Name   :  2. 继承与多态.py
@Description:  


@Create Time   :   2021/1/27 0027  10:17
@Author :   HaoWANG, Foshan，China
@Email  :   haowanghk@163.com

@Software : Pycharm
@Version: V1.0

"""

class Animal(object):   #编写Animal类
    def run(self):
        print("Animal is running...")

class Dog(Animal):  #Dog类继承Amimal类，有自己的run方法，覆盖父类的run（）方法
    def run(self):
        print('Dog is running...')
    pass

class Cat(Animal):  #Cat类继承Animal类，有自己的run方法，覆盖父类的run（）方法
    def run(self):
        print('Cat is running...')
    pass

class Car(object):  #Car类不继承，有自己的run方法，覆盖父类的run（）方法
    def run(self):
        print('Car is running...')

class Stone(object):  #Stone类不继承，也没有run方法
    pass

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Car())