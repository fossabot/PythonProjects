#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 09:07:17 2018

@author: jmat
"""

dct= {'name':'ravi', 'loc':'chennai'}
lst_of_tuple = lambda list: [  item for item in dct.items() ]

print(lst_of_tuple(dct))