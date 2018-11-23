# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 03:05:49 2018

@author: jmat
"""

c="Pandora's Box"
# c string will have index starting from 0 to 12.
print( "The 3rd character in ",c," is " ,c[2] )
print( "The 8th character in ",c," is " ,c[7] )

#Each character in the string will also be a string
print("5th Character is ",c[4]," and its datatype is ",type(c[4]))


#We can also do reverse indexing
print( "The Last character in ",c," is " ,c[12] )
print("The Last character by reverse indexing is ", c[-1])


#To extract more than one character use the below notation
print ("The first two characters are", c[0:2])

#We can avoid giving 0 as the first value and just give nothing.
#Python automatically takes 0 by default

print ("The first three characters are", c[:3])

#Similary we can avoid the last value too
print("The whole string without first two characters is" , c[3:]  )

print("The last three characters are", c[-3:])