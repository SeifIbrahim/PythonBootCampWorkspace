# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 14:13:58 2015

@author: home
"""
import math

class Polygon:
    def __init__(self, points):
        self.points = points
    def perimeter(self):
        temp = 0
        for i in range(0,len(self.points)):
            temp += math.sqrt((self.points[i][0]-self.points[(i+1)%len(self.points)][0])**2+(self.points[i][1]-self.points[(i+1)%len(self.points)][1])**2)
        return temp
        
a = Polygon([[0,-2],[1,1],[3,3],[5,1],[4,0],[4,-3]])
print(a.perimeter())