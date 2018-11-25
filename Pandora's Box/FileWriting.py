# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 11:55:45 2018

@author: jmat
"""

file=open("writing_example.txt","w")
file.write("Line 1")
#if you execute the above line in python console you get the length of characters you wrote to file
file.write("\nLine 2")
#if you dont close the file, the changes wont reflect in text file
file.close()