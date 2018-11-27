# Get the input from the user
# input

print('-' * 75)

# Get the string
string = input('Enter Any String -> ')
print('String ->', string, '->', type(string))

print('-' * 75)

# Get the number
num = input('Enter Any Number -> ')
num = int(num) if num.isdigit() else 'Not a Valid Number'
print('Number ->', num, '->', type(num))

print('-' * 75)

# Get the list
lst = input('Enter List of strings (separated by space) -> ').split()
print('List ->', lst, '->', type(lst))

print('-' * 75)

