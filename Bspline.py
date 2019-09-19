#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 13:20
# @Author  : HaoWANG
# @Site    : 
# @File    : Bspline.py
# @Software: PyCharm

import numpy as np
import scipy.interpolate as si


def bspline(cv, n=100, degree=3, periodic=False):
    """ Calculate n samples on a bspline

        cv :      Array ov control vertices
        n  :      Number of samples to return
        degree:   Curve degree
        periodic: True - Curve is closed
                  False - Curve is open
    """
    
    # If periodic, extend the point array by count+degree+1
    cv = np.asarray(cv)
    count = len(cv)

    if periodic:
        factor, fraction = divmod(count+degree+1, count)
        cv = np.concatenate((cv,) * factor + (cv[:fraction],))
        count = len(cv)
        degree = np.clip(degree,1,degree)

    # If opened, prevent degree from exceeding count-1
    else:
        degree = np.clip(degree,1,count-1)


    # Calculate knot vector
    kv = None
    if periodic:
        kv = np.arange(0-degree,count+degree+degree-1)
    else:
        kv = np.clip(np.arange(count+degree+1)-degree,0,count-degree)

    # Calculate query range
    u = np.linspace(periodic,(count-degree),n)


    # Calculate result
    return np.array(si.splev(u, (kv,cv.T,degree))).T

# Testing
import matplotlib.pyplot as plt
colors = ('b', 'g', 'r', 'c', 'm', 'y', 'k')

cv = np.array([[ 50.,  50.],
   [ 38.,  62.],
   [ 23.,  47.],
   [ 47.,   22.],
   [ 40.,   4.],
   [ 10.,   10.]])

plt.plot(cv[:,0],cv[:,1], 'o-', label='Control Points')

file = open("./BslineData.txt",'w')

for d in range(1,6):
    p = bspline(cv,n=100,degree=d,periodic=False)
    x,y = p.T
    file.write('X:'+'degree ='+str(d)+ '\r\n'+str(x)+'\r\n')
    file.write('Y:'+'degree ='+str(d)+ '\r\n'+ str(y)+'\r\n')
    plt.plot(x,y,'k-',label='Degree %s'%d,color=colors[d%len(colors)])
file.close()

plt.minorticks_on()
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0, 65)
plt.ylim(0, 65)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
print(x,y)
# END