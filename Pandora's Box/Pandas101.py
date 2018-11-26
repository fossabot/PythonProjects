# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 21:14:42 2018

@author: jmat
"""

import pandas
df1=pandas.DataFrame([ [2,4,6],[10,20,30] ])
print("The data frame is\n",df1)
print("Its type is ",type(df1))


df2=pandas.DataFrame([ [2,4,6],[10,20,30]],columns=["Price","Age","Value"])
print("The data frame df2 is\n",df2)
print("Its type is ",type(df2))



df3=pandas.DataFrame([ [2,4,6],[10,20,30]],columns=["Price","Age","Value"],index=["First","Second"])
print("The data frame df3 is\n",df3)
print("Its type is ",type(df3))

print ("We can access the columns like this\n", df3.Price)
dictionary_df4=pandas.DataFrame( [ {"Name":"Elliot","Surname":"Alderson","Alias":"Mr.Robot" },{"Name":"Edward","Surname":"Snowden"}])
print("The dictionary data frame df4 is\n",dictionary_df4)
print("Its type is ",type(dictionary_df4))


#dir(df1)

print("The mean of df1 data frame is\n",df1.mean())
print("the mean will have a data type " , type(df1.mean()) )

print("The mean of mean of df1 data frame is\n",df1.mean().mean())
print("the mean of mean will have a data type " , type(df1.mean().mean() ) )

print("The max of df3 data frame is\n",df3.Price.max())
print("the max will have a data type " , type(df3.Price.max() ) )


