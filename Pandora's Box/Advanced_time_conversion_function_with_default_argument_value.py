# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 18:47:44 2018

@author: jmat
"""


def time_conversion(minutes,seconds=3600):
    minutes=float(minutes)
    seconds=float(seconds)
    hours= minutes/60 + seconds /3600
    return hours

m=input ("Enter the ETA towards your next project deadline(minutes) : " )

print ("You should get working soon.I have added one extra hour to give you some wiggle time ", time_conversion(m), "hours")