# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 20:05:56 2018

@author: jmat
"""

import json
import difflib
<<<<<<< HEAD
data=json.load( open("data.json","r") )
=======
data=json.load( open("076 data.json","r") )
>>>>>>> master

def meaning(word):
    word=word.lower()
    close_word=get_close_matches(word,data.keys(),1,0.8) 
    if word in data:
        return data[word]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(close_word)> 0:
        print ( "Did you mean %s instead? " %close_word[0] )
        close_choice=input("Press Y for yes or N for no: ")
        close_choice_low=close_choice.lower()
        if close_choice_low == "y":
            return data[close_word[0]] 
        elif close_choice_low  == "n":
            return "Sorry!  I cant seem to find your word in my dictionary"
        else:
            return "Sorry ! We didnt understand your Query" 
    else:
        return "Sorry!  I cant seem to find your word in my dictionary"

word=input("Enter the word:")
mean=meaning(word)
if type(mean) == list:
    j=1
    for i in mean:
        print("Dictionary Entry ", j," : ", i)
        j=j+1
else: 
    print(mean)
