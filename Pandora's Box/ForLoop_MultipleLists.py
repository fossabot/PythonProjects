# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 11:08:27 2018

@author: jmat
"""

print("Printing out the data stored" )
name=["Elliot","Zeus","Sherlock"]
email_domains=["gmail","hotmail","yandex"]
for i,j in zip(name,email_domains) :
    print("\n\t Name: ", i ," \n\t Domain: ", j )
