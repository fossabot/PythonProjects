# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 14:22:21 2018

@author: jmat
"""

temperatures=[10,-20,-289,100]
 
def writer(temperatures, filepath):
    with open(filepath, 'w') as file:
        for c in temperatures:
            if c>-273.15:
                f=c*9/5+32
                file.write(str(f)+"\n")

writer(temperatures, "temp_conversion_Optimised_FileMethod.txt")