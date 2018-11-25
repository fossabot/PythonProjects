# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:54:49 2018

@author: jmat
"""

import datetime

present=datetime.datetime.now() 
print(type(datetime.datetime.now()))

birthday=datetime.datetime(1995,2,26,12,00,00,00)
delta=present-birthday
#print(delta)
print("You are ",delta.days," days old")
print (delta.total_seconds() , " seconds")