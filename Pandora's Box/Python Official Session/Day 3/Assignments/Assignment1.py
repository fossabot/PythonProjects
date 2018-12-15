#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 17:41:31 2018

@author: jmat
"""
freq_dct = dict()
freq_dct = {}

str1=input("Please Enter a String:")
#str1="Hello"
str2=[]
for i in str1:
    if i not in freq_dct:        
        freq_dct.update( {i:1} )
    else:
        freq_dct[i]+=1

print(freq_dct)
    


