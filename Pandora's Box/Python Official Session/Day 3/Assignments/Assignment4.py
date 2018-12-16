#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 09:26:16 2018

@author: jmat
"""

import re

print('-' * 75)



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

#write_file("Assignment4.txt", 'w')

valid_mail_lst=chk_pattern('[._]' + '[0-9][0-9][0-9]'+'@allstate.com')
print("Valid Mail IDs")
for i in valid_mail_lst:
    print(i)
    