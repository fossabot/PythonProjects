# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 12:01:47 2018

@author: jmat
"""


file=open("writing_example_withLoops.txt","w")
i=1
while i <=20:
    #line_content="Line"+str(i)
    if i ==1:
        file.write("Line "+str(i))
    else:
        file.write("\nLine "+str(i))
    i=i+1
file.close()