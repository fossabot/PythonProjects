#!/usr/bin/python
import re

line = "Elephants are smarter than Cats are smarter than dogs are smarter than lion";

matchObj = re.match( r'(cats).*(dogs)', line, re.M|re.I)
if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
   print (matchObj.group(0))
   print (matchObj.group(1))
   print (matchObj.group(2))
else:
   print ("No match!!")

#searchObj = re.search( r'dogs', line, re.M|re.I)
#if searchObj:
#   print ("search --> searchObj.group() : ", searchObj.group())
#else:
#   print ("Nothing found!!")
