#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 16:22:07 2018

@author: jmat
"""
import re
data_fname="Assignment6.txt"
with open(data_fname) as fread:
    #print('Read 4 ->', fread.read())
    string=fread.read()
    
print('Searching word ->', re.findall(r'\b[a-zA-Z][a-zA-Z]\b', string))