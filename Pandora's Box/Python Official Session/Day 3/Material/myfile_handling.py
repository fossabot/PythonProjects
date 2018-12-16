#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 19:06:10 2018

@author: jmat
"""

# File Handling

print('-' * 75)

'''
expandtabs - translate tabs to spaces
splitlines - split based on \n
'''

# Primary Modes - r(read mode - default), w(overwritten mode) and a(append mode)

# Function to implement w and a modes

# Filename
data_fname = "/root/Desktop/PythonProjects/PythonProjects/Pandora's Box/Python Official Session/Day 3/Assignments/Assignment8.txt"


# Use of 'with' block using read mode
file=open(data_fname,"w")
for i in range(1,101):
    file.write("Line "+str(i) + '\n')
file.close()




