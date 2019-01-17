# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 20:24:44 2019

@author: jmat
"""
import time
from datetime import datetime as dt
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.google.com","google.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working Hours")
    else:
        print("Fun Hours")
    time.sleep(5)
    