# Modules and Packages
# Modules - Enhances Reusability
# Easy to Modify

# When the user imports the module using from <module> import *
# only the functions/var/class which is mentioned in __all__ will be imported
__all__ = ['val_mail_id', 'get_count_char']

# Validate the mail id
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

# Retrieve the Palindrome
get_palin = lambda lst: [e for e in lst if e == e[::-1]]

if __name__ == '__main__':
    print('-' * 75)

    print('Mail Id ->', val_mail_id('from_utils@cypress.com'))

    print('-' * 75)

# Count the number of characters
get_count_char = lambda lst: [{ch: elem.count(ch) for ch in elem} for elem in lst]

