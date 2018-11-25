# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 13:04:57 2018

@author: jmat
"""

file=open("writing_example_with_lists.txt","w")
numbers=[1,2,3]
for i in numbers:
    file.write(str(i)+"\n")
file.close()