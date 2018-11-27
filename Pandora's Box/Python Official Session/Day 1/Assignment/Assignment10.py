# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 21:45:49 2018

@author: jmat
Q.Write a Python program which iterates the integers from 1 to 50. 
For multiples of three print "Foo" instead of the number and for the multiples of five print "Boo". 
For numbers which are multiples of both three and five print "FooBoo".
"""
for i in range (1,51):
    if i %15 ==0:
        print("FooBoo")
    elif i%5==0:
        print("Boo")
    elif i%3==0:
        print("Foo")
    else:
        print(i)
