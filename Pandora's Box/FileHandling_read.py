# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 16:52:29 2018

@author: jmat
"""

file=open("example.txt","r")
content=file.read()
print("The content of the file taken with read() is\n",content," \nand its data type is", type(content))
file.close()