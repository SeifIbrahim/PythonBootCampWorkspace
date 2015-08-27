# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 10:10:24 2015

@author: home
"""

import numpy as np
import matplotlib.pyplot as plt
from pylab import *

f =  lambda x : x**2
x = np.linspace(0,3,100)
y = f(x)

def trapz(x,y):
    sum = 0
    for i in range(0,len(x)-1):
        sum+=(x[i+1]-x[i])*(y[i+1]+y[i])
    return sum/2
    
def trapzf(f, a ,b , npts=100):
    x = np.linspace(a,b,npts)
    y = f(x)
    return trapz(x,y)
plt.plot(x,y)
print("My answer: "+str(trapzf(lambda x : x**2,0,3)))
print("Numpy answer: "+str(np.trapz(y,x)))