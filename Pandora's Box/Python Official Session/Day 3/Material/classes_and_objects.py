# Classes and Objects

'''
Class - A template that contains the common properties and methods
        that can be used by its objects

Object - An instance of the class

class classname(object) -> here, the object refers to the class which is present in
builtins.py and it contains the definition of predefined methods and variables
that can be re-used by all the user defined classes

Decorator -> Nested Functions which is used to perform pre and post activities
             during the execution of a function
'''

print('-' * 75)

# Class
class Subscriber(object):
    subs_name = 'ravi'
    subs_type = 'prepaid'

    # Initialize the object
    def __init__(self, subs_name, msisdn, subs_type='prepaid', bal=500):
        print('Initializing the object')
        self.subs_name = subs_name
        self.subs_type = subs_type
        self.msisdn = msisdn
        self.__bal = bal

    # Display the object in string format
    def __str__(self):
        subs_name = Subscriber.subs_name + ' shasthri'
        return '{} whose msisdn is {} of type {}'.format(subs_name,
                                                         self.msisdn,
                                                         self.subs_type)

    # Get the balance
    def get_balance(self):
        self.upd_balance(500)
        print('Static Method ->', Subscriber.proc_name())
        print('Class Method ->', self.get_details())
        return self.__bal

    # Modify the balance
    def upd_balance(self, amt):
        self.__bal += amt
        return self.__bal

    # Get the details
    @classmethod
    def get_details(self):
        return '{} -> {}'.format(self.subs_name,
                                 self.subs_type)

    # Use string methods
    @staticmethod
    def proc_name():
        return Subscriber.subs_name.upper(), len(Subscriber.subs_name)
    

#------------------------- END OF CLASS DEFINITION --------------------------#

# Name of the module
print('Module Name ->', __name__)

# Define the instances
print('Creating obj_1')
obj_1 = Subscriber('clark', '7654321098', bal=1000)    # num_list = list()

print('-' * 75)

print('Creating obj_2')
obj_2 = Subscriber('tris', '6543210987', 'postpaid', bal=3000)

print('-' * 75)

# Display the objects
print('Object 1 ->', obj_1)
print('Object 2 ->', obj_2)

print('-' * 75)

# Display subscriber name
print('Using Class ->', Subscriber.subs_name)
print('Using obj_1 ->', obj_1.subs_name)
print('Using obj_2 ->', obj_2.subs_name)

print('-' * 75)

# Balance
print('Object 1 Balance ->', obj_1.get_balance())
print('Increasing the balance ->', obj_1.upd_balance(500))

print('-' * 75)

# Get the details
print('Object 2 Details ->', obj_2.get_details())

print('-' * 75)

# proc_name
print('Using Class ->', Subscriber.proc_name())
print('Using Object ->', obj_1.proc_name())

print('-' * 75)


