# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 13:05:39 2018

@author: jmat
"""

#file=open("example.txt",'r')
#content=file.readline()
#print(content,end='')
#
#content=file.readline()
#print(content,end="")
#print("The second character of first word is ", content(1,2)



#file=open("example.txt",'r')
#content=file.readline()
#print(content,end='')
#
#content=file.readline()
#print(content,end="")

file=open("example.txt",'r')
file.seek(0)
for i in file:
    print (file.readline())
file.close()