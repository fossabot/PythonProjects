# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 14:03:05 2018

@author: jmat
"""

with open("example_with_statement.txt","a+") as file:
    file.seek(0)
    content=file.read()
    file.write("\nLine 7")
 
    