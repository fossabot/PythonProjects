# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 15:21:52 2018

@author: jmat
"""

get_count_char=lambda lst: [{ ch : elem.count(ch) )for ch in elem }for elem in lst]
lst_of_dicts=get_count_char(["php","aaa","bcc"])
print("List of dictionaries",lst_of_dicts)
for elem in lst_of_dicts:
    print("Element-->",elem)
    