# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
first = True
str= ""
sentence = ""

while str!="." and str!="?" and str!="!":
    str = input("Please enter a word in the sentence (enter . ! or ? to end): ")    
    
    if first or str=="." or str=="!" or str=="?": # If it is first or last don't put space
        sentence += str
        first = False
    else:
        sentence +=  " " + str   
    
    print("...currently: " + sentence)

print ("--->"+sentence)