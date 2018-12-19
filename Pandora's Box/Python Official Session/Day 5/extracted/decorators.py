'''
Decorators - Nested Functions (Closures)
Are used to avoid repetancy of lines of code
'''

import re
import time

def set_delay(delay):
    def measure_time_taken(f_name):
        def exec_function(*args, **kwargs):
            start_time = time.time()
            f_return = f_name(*args, **kwargs)
            time.sleep(delay)
            end_time = time.time()
            diff = str(round(end_time - start_time, 2)) + ' seconds'
            print(f_name.__name__ + ' took ' + diff + ' to complete')

            return f_return
        return exec_function
    return measure_time_taken

@set_delay(3)
def val_mail_id(mail_id, pattern):
    status = 'Invalid Mail Id'

    if re.search(pattern, mail_id):
        status = 'Valid Mail Id'

    return status

@set_delay(2)
def get_palin(lst):
    palin_lst = []

    for elem in lst:
        if elem == elem[::-1]:
            palin_lst.append(elem)

    return palin_lst

@set_delay(5)
def display_usr():
    return 'Welcome to Decorators'

if __name__ == '__main__':
    print('-' * 50)

    print('Mail Id ->', val_mail_id('justi.528@cypress.com',
                                    pattern='[a-z]{5}[._]\d{3}@cypress\.com'))

    print('-' * 50)

    print('Palin List ->', get_palin(['php',
                                      '123',
                                      'mam']))

    print('-' * 50)

    # Use of callback
    print('Reference -> ', val_mail_id)
    print('Output ->', val_mail_id('a@mail.com', '\d{3}'))

    print('-' * 50)

    print('Display ->', display_usr())

    print('-' * 50)
