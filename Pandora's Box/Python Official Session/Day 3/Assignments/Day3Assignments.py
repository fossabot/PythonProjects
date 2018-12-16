#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 22:49:11 2018

@author: jmat
"""

import re

"""
Q1.Get the string from the user. Count the number of each character from the string
"""
freq_dct = dict()
freq_dct = {}

str1=input("Please Enter a String:")
#str1="Hello"
str2=[]
for i in str1:
    if i not in freq_dct:        
        freq_dct.update( {i:1} )
    else:
        freq_dct[i]+=1

print(freq_dct)

"""
Q2.Simulating String Count Function
"""

def str_cnt(string, ch, start_pos=0, end_pos=-1 ):
    cur_pos=start_pos
    cnt=0
    if end_pos == -1 :
        end_pos=len(string)

    while True:
        cur_pos=string.find(ch,cur_pos,end_pos)
       # print(cur_pos)
        if cur_pos == -1:
            break
        else:
            cnt+=1
        cur_pos+=1
    print("No of occurences of",ch,"in ", string," with start pos",
          start_pos," and end position",end_pos," is "  ,cnt)

#str_cnt('phphp','hp',1,3)
#print ( str_cnt('php','p'))
#print("phphp".count("hp",1,3))


"""
Q3.Lambda expression that returns the list of key-value pairs from the dictionary
"""

dct= {'name':'ravi', 'loc':'chennai'}
lst_of_tuple = lambda list: [  item for item in dct.items() ]

print(lst_of_tuple(dct))

"""
Q4.Creating file that contains mail ids along with some other contents.
Validating mail ids in that file having patterns as follows

Starts with 5 alphabets followed by either '_' or '.' and followed by any 3 digits. The domain name should be 'allstate.com'
"""



def write_file(fname, fmode):
    # Open the file
    fhandle = open(fname, fmode)

    # Get the input from the user
    while True:
        line = input('Enter a Line -> ')
        if line.lower() == 'eof':
            break

        # Write the contents to the file
        fhandle.write(line + '\n')

    # Close the file
    fhandle.close()
    
# Check the pattern in the string
def chk_pattern(pattern):
    valid_mail=[]
    with open("Assignment4.txt") as fread:
        all_lines = fread.readlines()
        for i in all_lines:
            if re.search(pattern, i.strip("\n")):    # Case Sensitive
               valid_mail.append(i.strip("\n"))
            else:
                continue
        return valid_mail


#string="mohan%548@allstate.com"
#chk_pattern('[._]' + '[0-9][0-9][0-9]'+'@allstate.com' , string)

write_file("Assignment4.txt", 'w')

valid_mail_lst=chk_pattern('[._]' + '[0-9][0-9][0-9]'+'@allstate.com')
print("Valid Mail IDs")
for i in valid_mail_lst:
    print(i)
    

"""
Q5.Get the string from the user and validating whether it is aadhar/credit card number.  
"""

def chk_pattern(pattern, inp_string):
    if re.search(pattern, inp_string, re.I):   # Case Insensitive
        pass
    
    if re.search(pattern, inp_string):    # Case Sensitive
        return True

#inp_str="9876 5432 1098"
#inp_str="9876 4532 1098 6754"

inp_str=input("Please enter the number you want to check(Make sure to follow spacing)")
if chk_pattern('^(\d{4}\s){3}\d{4}$', inp_str)==True:
    print("The input is a Debit/Credi Card Number ")
if chk_pattern('^(\d{4}\s){2}\d{4}$', inp_str)==True:
    print("The number is a Aadhar Number ")
else:
    print("The input is neither Aadhar Card Number nor a Credit Card Number")

"""
Q6.Extracting only the two letter words from the file.    
"""

data_fname="Assignment6.txt"
with open(data_fname) as fread:
    #print('Read 4 ->', fread.read())
    string=fread.read()
    
print('Searching word ->', re.findall(r'\b[a-zA-Z][a-zA-Z]\b', string))

"""
Q7.Creating A Class 'Account' with given requirements 
"""
        
        
class Account(object):
    def __init__(self):
        
        try:
            self.acc_name=input("Enter the Account Name")
            self.acc_number=int (input("Enter the Account Number") ) 
            self.acc_branch=input("Enter the Account Branch")
            self.acc_type=input("Enter the Account Type")
            self.__bal= float(input("Enter the Balance"))
            print("Created the object\n",self)
        except (TypeError,AttributeError,ValueError) as er:
            print("You have entered a wrong input.Exiting...")
            print("Traceback\n",er)
    def __str__(self):
        return '{} has {} account in Branch {} with Account number {} '.format(self.acc_name,
                                                         self.acc_type,
                                                         self.acc_branch,self.acc_number)
    def get_balance(self):
        return self.__bal
    
    def __withdraw(self):
        if int(self.__bal)< 5000:
            print("Balance is less than 5000. Cannot withdraw from this account")
        else:
            amt=input("Enter Amount do you want to withdraw ?")
            print("You have successfully withdrawn" ,amt, " from your account")
            self.__bal=self.__bal-float(amt)
            print("Your main balance is now",self.__bal)
            
    def __deposit(self):
        amt=input("Enter Amount do you want to deposit ?")
        print("You have successfully deposited" ,amt, " to your account")
        self.__bal=self.__bal+float(amt)
        print("Your main balance is now",self.__bal)
        
    def fun(self):
        ##Can Implement Pin validation here
        a=input("Which Operation do you want to do(d for deposit/w for withdraw): " )
        if a == "d" or a== "D":
            self.__deposit()
        elif a=="w" or a=="W":
            self.__withdraw()
        else:
            print("You have entered wrong input")
        

obj_1=Account()

#obj_1=Account("John","5432","USA","Savings",2000)
#print( obj_1.acc_name, obj_1.acc_number , obj_1.acc_branch , obj_1.acc_type,obj_1.get_balance())


obj_1.fun()
print("\nAfter updation, the values are\n",obj_1)
#print( obj_1.acc_name, obj_1.acc_number , obj_1.acc_branch , obj_1.acc_type,obj_1.get_balance())


"""
Q8.Create the file which contains 50 to 100 lines depends on the user input and extracting required info
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