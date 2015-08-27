# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 18:17:45 2015

@author: home
"""
import pandas as pd
import numpy as np
import pylab
trends = pd.read_csv("trends.csv",index_col=0,parse_dates=True)

trends.plot(figsize=(15,15))
pylab.show()

keys = ['textbooks','spring_break','kayak','skiing','global_warming']
for key in keys:
    print(key + ':')
    for year in range(2004,2015):
        sub_trend = trends[trends.index.year == year]
        trend = sub_trend[key]
        
        peak_start_timestamp = sub_trend[trend == max(trend)].index[0]
        peak_start = str(peak_start_timestamp.month) + '-' + str(peak_start_timestamp.day)
        peak_week = str(peak_start_timestamp.week) 
        peak_end = sub_trend[trend == max(trend)].week_end[-1]
        peak_end = peak_end[5:].lstrip('0') #take off the left 0 of the month

        min_start_timestamp = sub_trend[trend == min(trend)].index[0]
        min_start = str(min_start_timestamp.month) + '-' + str(min_start_timestamp.day)
        min_week = str(min_start_timestamp.week)
        min_end = sub_trend[trend == min(trend)].week_end[0]
        min_end = min_end[5:].lstrip('0') 
        
        print('  in ' + str(year) + ' were highest from ' + peak_start + ' to ' + peak_end + " (Week " + peak_week + ")")
        print('          were lowest from ' +  min_start + ' to ' + min_end + " (Week " + min_week + ")")
        
def std_median(data):
    return np.sqrt( np.sum( (data - data.median())**2 ) * 1.0/ len(data) )

print(trends.spring_break.std(), std_median(trends.spring_break))
print(trends.textbooks.std(), std_median(trends.textbooks))
print(trends.skiing.std(), std_median(trends.skiing))
print(trends.kayak.std(), std_median(trends.kayak))
print(trends.global_warming.std(), std_median(trends.global_warming))

result = np.correlate(trends['spring_break'],trends['skiing'], mode='full')
gap = np.arange(result.size) - result.size/2
pylab.plot(gap,result)
pylab.show()

result2 = np.correlate(trends.global_warming,trends.skiing, mode='full')
gap2 = np.arange(result2.size) - result2.size/2
print(gap2[result2.argmax()])
pylab.plot(gap2,result2)
pylab.show()