# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 21:50:20 2018

@author: jmat
Q.From the string "Monty Python's Flying Circus"
 display the words along with its length
"""

str1="Monty Python's Flying Circus"
str2=str1.split()
for i in str2:
    print("\n Word:" ,i , "\nLength : ", len(i)  )