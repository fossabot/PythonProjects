#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 17:39:21 2018

@author: jmat
"""

fname=input("Enter the name of the file to be created:")
fhandle = open(fname, "w")

# Get the input from the user
while True:
    line = input('Enter a Line to be stored in file(eof to exit)-> ')
    if line.lower() == 'eof':
        break
    fhandle.write(line + '\n')

fhandle.close()

#fname="Assignment8.txt"
with open(fname) as fread:
    str1=fread.readlines()
str1=[i.rstrip("\n") for i  in str1]

print("First 10 Lines of the File")
for i in range(0,10):
    print(str1[i])
    
print("Last 10 Lines of the File")
for i in range(1,11):
    print(str1[-i])    

start=int( input("Enter the start range:") )
end=int ( input("Enter the end range:") )
print(" Lines in between the range")
for i in range(start-1,end):
    print(str1[i])

print("Even Lines of the File")
for i in range(1,len(str1),2):
    print(str1[i])

print("Odd Lines of the File")
for i in range(0,len(str1),2):
    print(str1[i])

ch=input("Enter the character to be searched for:")
for i in range(0,len(str1)):
    if str1[i].find(ch) != -1:
        print(str1[i])