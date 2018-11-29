# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 22:31:38 2018

@author: jmat
Description: Python Day 1 Assignments
"""



"""
Q1.Write a Python program to calculate the length of a string
"""

string=input("Please enter a string")
print("The length of the string ", string," is ", len(string))



"""
Q2. Write a Python program to count the number of characters (character frequency) in a string.
"""

str1=input("Please Enter a String")
#str1="Hello"
freq_lst=[ ]
str2=[]
for i in str1:
    if i not in str2:
        str2.append(i)
        freq_lst.append( str1.count(i) )

for i in range(0,len(str2) ) :
    print("Character:", str2[i] ,"-->Frequency:", freq_lst[i] )



"""
Q3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
    If the string length is less than 2, return instead of the empty string.
"""

str1=input("Enter a string")
if len(str1)>2:
    str2=str1[:2]+str1[-2:]
    print("The required String is",str2)
else:
    print("Insufficent Length for String to perform operation on")



"""
Q4.Write a Python program to get a single string from two given strings, separated by a space and also
  swap the first two characters of each string.
"""

str1=input ("Enter the first String")
str2=input("Enter the second String")
str1=str1[1]+str1[0]+str1[2:]
str2=str2[1]+str2[0]+str2[2:]
res_str=str1+" " + str2
print ("The required String is ", res_str)


"""
Q5.Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
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


"""
Q6.Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, 
if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. 
Return the resulting string.
"""



#str1="He is not a poor guy"
str1="He is poor but not because of his selfless deeds "
print("The string you have entered is :  ",str1)
pos_not=str1.find("not")
pos_poor=str1.find("poor")
print("\nThe first occurence of \"not\" in the string at", pos_not+1 ,"position")

print("\n The first occurence of \"poor\" in the string at", pos_poor+1 ,"position")

if pos_poor < pos_not:
    str1=str1[:pos_poor]+"good"+str1[pos_not+3:]
print(str1)


"""
Q7.Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
"""

print("Numbers divisible by 7 and 5 in the range 1500 and 2700 (both included) are as belows")
for i in range (1500,2701):
    if i % 35 == 0:
        print(i)

"""
Q8.Write a Python program that accepts a word from the user and reverse it.
"""

str1=input("Enter any String:  ")
print("The reverse string is  ",str1[::-1])



"""
Q9.Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
"""

for i in range(0,7):
    if not (i ==3 or i==6 ):
        print(i)

"""
Q10.Write a Python program which iterates the integers from 1 to 50. 
For multiples of three print "Foo" instead of the number and for the multiples of five print "Boo". 
For numbers which are multiples of both three and five print "FooBoo".
"""
for i in range (1,51):
    if i %15 ==0:
        print("FooBoo")
    elif i%5==0:
        print("Boo")
    elif i%3==0:
        print("Foo")
    else:
        print(i)


"""
Q11.Prompt the user to input a value, until user enters some text.
"""

str1=""
while str1.isdigit()==False:
    str1=input("Enter a Value (int) ")

"""
Q12.From the string "Monty Python's Flying Circus"
 display the words along with its length
"""

str1="Monty Python's Flying Circus"
str2=str1.split()
for i in str2:
    print("\n Word:" ,i , "\nLength : ", len(i)  )

"""
Q13. Prompt the user to input any numbers between 1 and 9. 
If User enters any other number, prompt the user to input again.
If the user enters valid input, display the pattern mentioned.
"""

k=-1
while k==-1:
    str1= input("Enter a value(1-9)") 
    if str1.isdigit()==True:
        str1=int(str1)
        k=1
        for i in range(0,str1) :
            for i in range(0,str1):
                print("*",end="")
                i-=1
            print("")
            str1-=1
        
    
"""
Q14.Take a list of strings. Filter the list which contains only palindrome
"""

lst=['php', 'perl', 'mam']
for i in lst:
    if i == i[::-1]:
        pass
    else:
        lst.remove(i)
print(lst)

"""
Q15.Get the number from the user. Generate the list of square of 'n' numbers
"""
k=-1
lst=[]

while k==-1:
    str1= input("Enter an integer") 
    if str1.isdigit()==True:
        str1=int(str1)
        k=1
        for i in range(1,str1) :
            lst.append(i**2)
            str1-=1
print(lst)