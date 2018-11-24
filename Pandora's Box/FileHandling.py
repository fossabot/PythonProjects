# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 16:15:40 2018

@author: jmat
"""

file=open("example.txt","r")
print ("The type of the file pointer is", type(file))
print("The contents of the file opened is")
for i in file:
    print ("\n ",i)
    print (type(i))
file.close()