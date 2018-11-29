# Exception Handling

import traceback as tb

print('-' * 75)

try:
    print('string')
    print(1/1)
    print(2 + int('3'))

    try:
        # num, string = 1,  # ValueError
        raise FileNotFoundError('Insufficient Values provided by User')
    except NameError as ne:
        print('NE Occurred ->', ne)
        
    
except (NameError, ZeroDivisionError) as ce:
    print('CE Occurred ->', ce)
    
except TypeError as te:
    print('TE Occurred ->', te)

except Exception as e:
    print(tb.format_exc())
    print(e.__class__.__name__ + ' -> ' + str(e))

else:
    print('No Exceptions')

finally:
    print('Always be Executed')


print('After Statements')

print('-' * 75)

import re

# User Defined Exceptions
class InvalidMobileNumber(Exception):
    def __init__(self, mobile):
        self.mobile = mobile
        self.err_msg = 'User has entered an Invalid Mobile Number -> '

    def display_err_msg(self):
        return self.err_msg + self.mobile

try:
    mob_num = input('Enter Mobile Number -> ')
    
    if re.search('^[6-9]\d{9}$', mob_num):
        print('Valid Mobile Number ->', mob_num)
    else:
        raise InvalidMobileNumber(mob_num)

except InvalidMobileNumber as imn:
    print(imn.display_err_msg())
    
print('-' * 75)

