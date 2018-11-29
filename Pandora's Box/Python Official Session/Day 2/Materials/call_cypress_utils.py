print('-' * 75)

'''
Whenever the module is being imported, it will check in the following dirs:
a) Current Directory (Highest Priority)
b) Library Directory
c) Permanent Changes:
   Directories set in PYTHONPATH environmental variable

   Windows:
   dir1;dir2;dir3 (Works exactly as PATH environmental variable)
   If python is installed in program files, system variables needs to be modified
   If python is installed in user directory, user variables needs to be modified

   UNIX Flavours:
   dir1:dir2:dir3 (Works exactly as PATH environmental variable)

   Temporary Changes:
   import sys
   sys.path - List Variable
'''

import sys
print('All Path ->', sys.path)

sys.path.insert(0,
                '/Users/kanish/Training/Cypress_Python_Nov2018/Day_2_28Nov2018/modules')

print('-' * 75)

print('Updated Path ->', sys.path)

print('-' * 75)

import cypress_utils as cu
from cypress_utils import *

'''
def val_mail_id(mail_id):
    pass
'''

print('Current Module ->', dir())

print('-' * 75)

print('From Cypress Utils ->', dir(cu))

print('-' * 75)

print('Document ->', val_mail_id.__doc__)

print('-' * 75)

# Validate Mail Id
print('Mail Id ->', val_mail_id('justin@cypress.com'))

print('-' * 75)

# Get Palin
print('Palin List ->', cu.get_palin(['madam', 'aaaaa']))

print('-' * 75)

# Count Char
print('Count Char ->', get_count_char(['madam', 'aaaaa']))

print('-' * 75)

# __init__.py -> in each and every directory to consider the directory
# as a package => prior to python 3.7
from welcome.script.user_details import display_user
print('Display User ->', display_user('Raj'))

print('-' * 75)

