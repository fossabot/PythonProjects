# Functions
# Re-usability


'''
Function to validate the mail id
Criteria 1 -> Username should be of atleast 5 characters
Criteria 2 -> Domain name should be 'cypress.com'

user@cypress.com -> cypress.com
usern@cypress.com -> @cypress.com
username@cypress.com -> ame@cypress.com

Function Returns single value -> Type of return value
Function Returns multiple values -> Type is Tuple
'''

print('-' * 75)

def val_mail_id(mail_id):
    
    '''
    Purpose: To Validate the Mail id
    Criteria 1 -> Username should be of atleast 5 characters
    Criteria 2 -> Domain name should be 'cypress.com'

    I/P Params -> Mail Id
    O/P Params -> Status
    '''
    
    status = 'Valid' if mail_id.endswith('@cypress.com', 5) else 'Invalid'
    return status, mail_id.split('@'), len(mail_id.split('@'))

# Invoke the function
ret = val_mail_id('davies@cypress.com')

# Identity Operator
if ret is not None:
    print('Return ->', ret, '->', type(ret))
else:
    print('Function does not return any values')

print('-' * 75)

# Document String
print('Document String ->', val_mail_id.__doc__)

print('-' * 75)

# Module Level Documentation
print('Module Document ->', __doc__)

print('-' * 75)
