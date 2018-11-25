# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 19:05:00 2018

@author: jmat
"""
import datetime

now=datetime.datetime.now()

def format_time_for_name(filename):
    correct_format=now.strftime("%Y-%m-%d-%H-%M-%S-%f.txt")
    return (correct_format)
def create_file():
    name=format_time_for_name(now)
    with open(name,"w") as file:
        file.write("")

#format_time_for_name()
create_file()