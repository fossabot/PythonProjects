# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 11:49:37 2018

@author: jmat
"""


file=open("fruits.txt","r")
content=file.readlines()
print("Length of each line")
for i in content:
    print( len (i.rstrip("\n") ) )
file.close()