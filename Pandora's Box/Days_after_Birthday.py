# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 19:20:53 2018

@author: jmat
"""
import datetime

birthday=datetime.datetime(1995,2,26,12,00,00,00)

after=birthday+datetime.timedelta(days=314)
print("314 days from your birthday is ",after )