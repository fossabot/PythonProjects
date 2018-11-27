# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 21:16:36 2018

@author: jmat
Q.Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
"""

print("Numbers divisible by 7 and 5 in the range 1500 and 2700 (both included) are as belows")
for i in range (1500,2701):
    if i % 35 == 0:
        print(i)
        