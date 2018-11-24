# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 16:55:27 2018

@author: jmat
"""


file=open("example.txt","r")
content=file.readlines()
print("The content of the file taken with read() is\n",content," \nand its data type is", type(content))
file.close()
print("Removing the newline characters")
#List comprehension
content=[i.rstrip("\n") for i  in content]
print("Here is the new data\n", content)