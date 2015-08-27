# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 12:02:28 2015

@author: home
"""

import random
import numpy

voc = ["x","x","+","/","1","2","3"]

nfunc = 1000000
maxchars = 10
eval_places = numpy.arange(-3,3,0.4)
sin_val = eval_places**2 + eval_places
minimum = numpy.inf
Y = 0
result = 0
tries = []
for i in range (1,nfunc):
    funcstr="".join(random.choice(voc,random.randint(),maxchars))+"\n"
    lambdafunc="Y = lambda x:"+funcstr +"\n"
    lambdafunc+="result = Y(eval_places)"
    try:
        exec(funcstr)
    except:
        continue    
    try: 
        tries.append(((abs(result - Y).sum()) ,funcstr))
        if (abs(result - Y)).sum() < 0.0001:
            break
    except:
        pass
    del result
    del Y
print (tries)