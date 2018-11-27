# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 20:26:22 2018

@author: jmat
Q.Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing' then add 'ly' instead. 
If the string length of the given string is less than 3, leave it unchanged.
"""

#str1="Helloing"
str1=input("Enter String to perform operation on:")
print("\n\n The String you have entered is: ",str1)
if str1.endswith("ing")==True:
    str1=str1+"ly"
elif len(str1)>=3:
    str1=str1+"ing"
else:
    print("""String length is less than 3 and required operation cannot be performed.
           New string will be the orginal string itself """)

print("The New string will be ",str1)