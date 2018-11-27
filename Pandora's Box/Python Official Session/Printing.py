# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 09:43:31 2018

@author: jmat
"""
##USing Repetition Charcter with Printing
print("-"*2)

##By default giving operands with spaces will give a space in between 


print("Hack","the","Planet")

#you can override this space with the syntax below
print("Hello","World ",sep="-" )


##Overrid the defaul newline after each print statement
print("Hello","World ",sep="-" ,end=">")
print("I am JMAT")


# Variables (Dynaming Typing)

var =1
var =1.5

var ="a"

#String
var="Python"

##Boolean
var=True

print(type(var))

#to get just the Boolean  as output
print(type(var).__name__)

##any variable/methods which is starting and ending with double undersocrw are treated as predefine



#Checking the type of the type varaible itself
print(type( type(var) ) )
print(type( type(var).__name__ ))

#checking the data type
print("Method 1 using __name__ --> " ,type (var).__name__=="int")
print("MEthod 2 using type-->",type(var)==type(1))
print("Method 3 using instance--> ",isinstance(var,str))

##The below statement will retyrn as true since bool can be considered as 1 and 1 is an integer
print("Method 3 using instance--> ",isinstance(var,int))



##Multiple Values to a variable 

var =1,"string",True
print("Var is ", var,"and its type is ", type(var))

#Multiple Assignments 
num,string,test=1,"string",True

print("num is ", num,"and its type is ", type(num))

print("string is ", string,"and its type is ", type(string))


print("test is ", test,"and its type is ", type(test))

##Error 

#num,string,test=1,"string"
#num,string=1


num,string,test=var

print("num is ", num,"and its type is ", type(num))

print("string is ", string,"and its type is ", type(string))



print("test is ", test,"and its type is ", type(test))


##Multiple Line Strings
ml_string="""Line 1
Line 2
Line 3 """

print(ml_string,type(ml_string))
