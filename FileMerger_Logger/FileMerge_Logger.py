# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 19:35:03 2018

@author: jmat
"""
import glob2
import datetime 

now=datetime.datetime.now()

def format_time_for_name(filename):
    correct_format=now.strftime("%Y-%m-%d-%H-%M-%S")
    return (correct_format)
def create_file():
    name=format_time_for_name(now)
    return name
        
file_names=glob2.glob("*.txt")
print("The following files will be merged to a new file")
for x in file_names:
    print(x)

merger_name=create_file()
merger_file=open(merger_name+"_MergedLogs.txt","w")

for i in file_names:
    with open(str(i),"r") as temp:
        content=temp.read()
        merger_file.write(content+"\n")
    
merger_file.close()
