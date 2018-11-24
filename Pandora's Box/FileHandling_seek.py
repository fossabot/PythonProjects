# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 16:56:23 2018

@author: jmat
"""


file=open("example.txt","r")
#Starting from 3rd character from start
file.seek(3)

content=file.read()
print(content)

file.close()