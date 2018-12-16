#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 10:41:20 2018

@author: jmat
"""

import re
def chk_pattern(pattern, inp_string):
    if re.search(pattern, inp_string, re.I):   # Case Insensitive
        pass
    
    if re.search(pattern, inp_string):    # Case Sensitive
        return True

#inp_str="9876 5432 1098"
#inp_str="9876 4532 1098 6754"

inp_str=input("Please enter the number you want to check(Make sure to follow spacing)")
if chk_pattern('^(\d{4}\s){3}\d{4}$', inp_str)==True:
    print("The input is a Debit/Credi Card Number ")
if chk_pattern('^(\d{4}\s){2}\d{4}$', inp_str)==True:
    print("The number is a Aadhar Number ")
else:
    print("The inout is neither Aadhar Card Number nor a Credit Card Number")
#chk_pattern('^(\d{4}\s){3}\d{4}$', inp_str)  # Debit/Card Number
#chk_pattern('^(\d{4}\s){2}\d{4}$', inp_str)