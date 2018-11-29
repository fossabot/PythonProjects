'''
Inheritance - Using the properties of another class which is inherited

Class which is inherited - Parent/Base/Super
Class which is inheriting - Child/Derived/Sub
'''

print('-' * 75)

print('Single Inheritance')

class SI1:
    def __init__(self):
        print('In SI1')

class SI2(SI1):
    pass

obj = SI2()

print('-' * 75)

print('Hierarchial Inheritance')

class SI3(SI1):
    def __init__(self):
        print('In SI3')
        super(SI3, self).__init__()
        print('After Init')

obj = SI3()

print('-' * 75)

print('Multilevel Inheritance')

class ML1:
    def __init__(self):
        print('In ML1')

class ML2(ML1):
    pass

class ML3(ML2):
    def __init__(self):
        print('Calling Parent from ML3')
        super(ML3, self).__init__()

obj = ML3()

print('-' * 75)

print('Multiple Inheritance')

class MP1:
    def __init__(self):
        print('In MP1')

class MP2:
    class_var = 'its a class variable'
    
    def __init__(self):
        print('In MP2')
        self.ins_var = 'its an instance variable'

class MP3(MP2, MP1):
    def __init__(self):
        print('Calling Parent from MP3')
        MP1.__init__(self)
        self.ins_var = 'Child Variable'
        super(MP3, self).__init__()

obj = MP3()

print('Class Var ->', obj.class_var)
print('Instance Var ->', obj.ins_var)

print('-' * 75)

class Employee:
    def __init__(self, name):
        self.name = self.change_name(name + ' ' + get_name())

    def change_name(self, user):
        return user.upper()

def get_name():
    return input('Enter the Name -> ')

obj = Employee('mike')
print('Name ->', obj.name)

print('-' * 75)


