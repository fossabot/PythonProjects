# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 14:18:57 2018

@author: jmat
"""

def temp_conversion(temp):
    temp=float(temp)
    if temp<-273.15:
        return -1
    else:
        res= ( (9*temp)/5 ) +32
        return res
    

l=[10,-20,-289,100]
print("\n I have a list of celsius temperature at which you can fry your enemies to maximum pain: Here is the list:\n", l)
print("Here is the also temp in Fahrenheit incase you dont have a celsius thermometer. I will write them to a file for easier handling")
file=open("example_temp_fahrenheit.txt","w")
for i in l:
    new_temp=temp_conversion(i)
    if new_temp == -1:
        print("There seems to be some physically unobtainable temperature.I am not writting it to the file" )
    else:
        file.write(str(new_temp)+"\n" )
file.close()