# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 15:19:42 2015

@author: home
"""

import datetime

date =  datetime.datetime(2000,4,18)
deltadate = datetime.datetime.now() - date
print (deltadate.days)
print (deltadate.days%365)
print (datetime.datetime.now()+datetime.timedelta(1000))