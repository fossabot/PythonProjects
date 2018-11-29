# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 22:15:18 2018

@author: jmat
Q.Take a list of strings. Filter the list which contains only palindrome
"""

lst=['php', 'perl', 'mam']
for i in lst:
    if i == i[::-1]:
        pass
    else:
        lst.remove(i)
print(lst)
        