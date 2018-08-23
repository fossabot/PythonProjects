# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:32:24 2018

@author: jmat
"""
import pandas
df1=pandas.DataFrame([ [2,4,6], [10,20,30] ] )
df2=pandas.DataFrame([ [2,4,6], [10,20,30] ] ,index=["First","Second" ] ,columns=["Price","Age","Value"] )
df3=pandas.DataFrame([ {"Name":"John","Surname":"Doe"},{"Name":"Jack","Surname":"Reacher"} ] )
print(df1)
print(df2)
print(df3)
print( type(df1) )
df2.mean()
print ( type(df2.mean()) )
print(df2.Price)
print(df2.Price.mean())
print(df2.Price.max())