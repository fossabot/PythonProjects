# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 19:05:00 2018

@author: jmat
"""
import datetime

filename=datetime.datetime.now()

def create_file():
    with open(filename,"w") as file:
        file.write("")
