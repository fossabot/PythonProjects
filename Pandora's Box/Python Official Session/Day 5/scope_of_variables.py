# Scope of Variables

print('-' * 70)

def change_var():
    #global var
    #print('Top ->', var)
    var = 'php'
    print('2 ->', var)

def change_var_again():
    global  var
    var = 'perl'
    print('4 ->', var)

var = 'python'

print('1 ->', var)
change_var()
print('3 ->', var)
change_var_again()
print('5 ->', var)

print('-' * 70)

# Pass by Reference
def change_list(lst):
    lst.extend(range(6,11))
    lst = list(range(6, 11))
    print('In Function ->', lst)

num_list = list(range(1,6))
print('Before Function ->', num_list)
change_list(num_list[:])
print('After Function ->', num_list)

print('-' * 70)

def outer():
    scr_name = None

    def inner():
        nonlocal scr_name
        scr_name = 'python3'.split()

        def innermost():
            nonlocal  scr_name
            scr_name = {'script': 'python3.7.1'}

        innermost()

    inner()
    return scr_name

print('Nested ->', outer())

print('-' * 70)

# Function to calculate square
def sqr(n):
    return n ** 2

def cube(n):
    return n ** 3

def calc(func, n):
    return func(n)

# sqr = 2
# cube = 5

print('Square ->', calc(sqr, 5))
print('Cube ->', calc(cube, 5))

print('-' * 70)
