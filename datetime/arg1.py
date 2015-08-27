# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 15:34:03 2015

@author: home
"""

import sys
import datetime

if len(sys.argv) == 2:
    print (datetime.datetime.now()+datetime.timedelta(int(sys.argv[1])))
elif len(sys.argv) == 4:
    print (datetime.datetime.now() - datetime.datetime(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))