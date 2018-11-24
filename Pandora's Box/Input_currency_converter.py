# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 10:30:30 2018

@author: jmat
"""

def currency_converter(rate,euros):
    dollars=float(euros) *float(rate)
    return dollars

r=input("Enter the Currency rate: " )
e=input("Enter the Euros you have in hand: " )

print("Damn! Stash it somehwere before you loose it. You have ", currency_converter(r,e), "$ " )
