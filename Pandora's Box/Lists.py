# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 08:35:27 2018

@author: jmat
"""

#String is made of other strings/characters
#Lists can contain any other datatypes

c=["H",2,2,2.4,"Hello"]
print(c)

#We can also apply indexing like we did in strings

print("The second item is the list is ",c[1],"and its datatype is ", type(c[1]) )

print("The third item is the list is ",c[2],"and its datatype is ", type(c[2]) )

print("The first item is the list is ",c[0],"and its datatype is ", type(c[0]) )

#Splitting a list will again give you a list

print("The first 3 elements are ", c[0:3] ," and its datatype is ",type (c[0:3]) )

#To know more about list functions : dir(list) 
#To get more details use help(list.<fun> )

#To append items use append function
print ("Adding the name Neo to the list")
c.append("Neo")
print("After appending Neo the whole list will look like " , c)


#To remove items use remove function
print ("Removing the number 2 from the list")
c.remove(2)
print("After removing 2 , the whole list will look like " , c)
#Remove will only remove the first occurence of value


