# Description

'''
Python - Interpreted Language
Interpreter - Line by Line Execution

Who discovered Python and Why the name Python?
Discovered by Guido Van Rossum in early 1990s
Python is the name of the character played in "Monty Python's Flying Circus"

Anaconda Python => Package used for Data Analytics and Machine Learning Concepts

Areas we can implement python:
Automation
Data Analytics
Machine Learning
Cloud Computing
Web Designing
GUI Programming
'''

print('-' * 75)  # * => Repetition Operator

# Print Function
print('hello', 'people', sep='--', end='>>>')
print('welcome', 'to', 'python', 'scripting', sep=',')

print('-' * 75)

# Variables (Dynamic Typing)

'''
type function gives you what type of data it contains
No difference between single and double quotes
If any set of characters given in single/double quotes, it will be taken as string

Any variables/methods which is starting and ending with
__ (double underscore) are treated as predefined.
'''

var = 1
print(var, '->', type(var), '->', type(var).__name__)

var = 1.5
print(var, '->', type(var), '->', type(var).__name__)

var = 'A'
print(var, '->', type(var), '->', type(var).__name__)

var = "python"
print(var, '->', type(var), '->', type(var).__name__)

var = True
print(var, '->', type(var), '->', type(var).__name__)

print('-' * 75)

# Checking the data type
print('Method 1 using __name__ ->', type(var).__name__ == 'int')
print('Method 2 using type ->', type(var) == type(1))
print('Type of var ->', type(var))
print('Method 3 using isinstance ->', isinstance(var, str))

print('-' * 75)

# Multiple Values to a variable
var = 1, 'string', True
print(var, '->', type(var))

print('-' * 75)

# Multiple Assignments
# num, string, is_chk = 1, 'string'  # throws ValueError
num, string, is_chk = var
print(num, '->', type(num))
print(string, '->', type(string))
print(is_chk, '->', type(is_chk))

print('-' * 75)

# Multi Line Strings
ml_string = 'This is Line1\nThis is Line2\nThis is Line3'
print(ml_string, '->', type(ml_string))

print('-' * 75)

ml_string = """This is Line1
This is Line2
This is Line3"""
print(ml_string, '->', type(ml_string))

print('-' * 75)
