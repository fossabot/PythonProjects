# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 19:24:01 2018

@author: jmat
"""

import time
import datetime

lst=[]
for i in range(5):
    lst.append(datetime.datetime.now())
    time.sleep(1)

for i in lst:
    print (i)