# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 18:22:29 2018

@author: jmat
"""

def minutes_to_hours(minutes):
    hours=float(minutes) /60
    return hours

def minutes_to_seconds(minutes):
    sec=int(minutes)* 60
    return sec
min=input("Enter the Minutes:")
print("The corresponding Hours is " , minutes_to_hours(min)," hours ")
print("The corresponding seconds is " , minutes_to_seconds(min)," seconds ")