# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 18:38:33 2018

@author: jmat
"""

def time_conversion(minutes,seconds):
    minutes=float(minutes)
    seconds=float(seconds)
    hours= minutes/60 + seconds /3600
    return hours

m=input ("Enter the ETA towards your next project deadline(minutes) : " )
s=input ("You havent noted down the time to seconds! Ha Ha noob. Enter the seconds too:") 


print ("You should get working.You have got only  ", time_conversion(m,s), "hours")