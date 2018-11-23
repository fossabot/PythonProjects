# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 08:54:11 2018

@author: jmat
"""

d={"Name":"Neo","Address":"The Matrix","Nickname":"The One"}
print("The Dictionary is ",d)

#We can access items with custom indexes in a dictionary
print("Name is ",d["Name"])

#We can add lists/tuples to the dictionaru also

d={"Name":"Neo","Address":"The Matrix","Nickname":"The One","Cities":["New York","Japan","Tokyo"]}
print("\nAfter adding lists the new dictionary will look like \n", d)
print ( "The type of list element in dictionary is ", type(d["Cities"]))
print ( "The first element within the list is ", d["Cities"][0])

#Changing List to Tuples
d={"Name":"Neo","Address":"The Matrix","Nickname":"The One","Cities":("New York","Japan","Tokyo")}
print("\nAfter change, the new dictionary will look like \n", d)
print ( "The type of tuples element in dictionary is ", type(d["Cities"]))
print ( "The first element within the tuple is ", d["Cities"][0])