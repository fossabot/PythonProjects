# Strings
# Immutable Object

print('-' * 75)

string = 'Python is so much Efficient'
print(string, '->', type(string))

print('-' * 75)

# Indexing
# From left to right -> 0, 1, 2, 3 and so on
# From right to left -> -1, -2, -3 and so on

print('string[5] ->', string[5])
print('string[-9] ->', string[-9])
# print('string[100] ->', string[100])

print('-' * 75)

# Slicing
# string[start_index:end_index]

# If start_index is not specified -> by default it takes 0
# If end_index is not specified -> by default it takes length of the string

# If start_index and end_index are specified, start_index is inclusive
# end_index is exclusive

# start_index < end_index

print('string[:] ->', string[:])
print('string[:3] ->', string[:3])
print('string[3:] ->', string[3:])
print('string[3:21] ->', string[3:21])
print('string[-21:-3] ->', string[-21:-3])
print('string[-10:] ->', string[-10:])

print('-' * 75)

# string[si:ei:step_index]

# If step_index is +ve, it prints the characters from left to right
# If step_index is -ve, it prints the characters from right to left

# Whenever we do step index, the index should fall within the given range

print('string[::] ->', string[::1])
print('string[::-1] ->', string[::-1])

print('string[3:21:3] ->', string[3:21:3])   # Indexes 3, 6, 9, 15, 18
print('string[-3:-21:-3] ->', string[-3:-21:-3])

print('string[21:3:-3] ->', string[21:3:-3])
print('string[-21:-3:3] ->', string[-21:-3:3])

print('-' * 75)

# Functions
# generic which takes any type of parameters
print('Length ->', len(string))     # Returns the number of characters
print('Max ->', max(string))  # Returns the maximum character based on ASCII
print('Min ->', min(string))  # Returns the minimum character based on ASCII

print('-' * 75)

print('ASCII value of space ->', ord(' '))     # Returns ASCII Value
print('Character of 121 ->', chr(121))     # Returns the character

print('-' * 75)

# Methods (user defines the function inside the class)
# Which applies to the particular class

# Case Methods
print('Upper ->', string.upper())  # Converts all chars to uppercase
print('Lower ->', string.lower())  # Converts all chars to lowercase
print('Capitalize ->', string.capitalize()) # Only first character in uppercase
                                            # Rest all characters in lowercase
print('Title ->', string.title())  # Converts first letter of all words in upper

print('-' * 75)

# Is Methods
print('isupper ->', string.upper().isupper())
print('islower ->', string.lower().islower())
print('isdigit ->', '528@gmail.com'.isdigit())
print('isalnum ->', '1@1'.isalnum())
print('isalpha ->', '1a1'.isalpha())

print('-' * 75)

# startswith
print('startswith Python ->', string.upper().startswith('PYTHON'))
print('starstwith on ->', string.startswith('on', 4, 20))
print('startswith on ->', string[4:20].startswith('on'))

print('-' * 75)

# endswith
print('endswith cient ->', string.endswith('cient'))
print('endswith on ->', string.endswith('on', 0, 6))
print('endswith on ->', string[0:6].endswith('on'))

print('-' * 75)

# Split
spt_str = string.split()   # splitted based on ' '
print(spt_str, '->', type(spt_str))

print('-' * 75)

print('Split using is ->', string.split('is'))

print('-' * 75)

# Join
joined_str = ' >> '.join(spt_str)
print(joined_str, '->', type(joined_str))

print('-' * 75)

print('Join from string ->', '--'.join(string))

print('-' * 75)

# Count
# counts the number of occurrences of the given character
print('No: of i ->', string.count('i'))
print('No: of is ->', string.count('is'))
print('No: of i b/w range ->', string.count('i', 3, 20))

print('-' * 75)

# Find
print('Position of i ->', string[string.find('i') + 1:].find('i'))
print('Position of on ->', string.find('on'))
print('Position of at ->', string.find('at'))

print('-' * 75)

# Index
print('Index of i ->', string.index('i'))
print('Index of on ->', string.index('on'))
# print('Index of at ->', string.index('at'))

print('-' * 75)

# Strip
string = ',@,,,python,scripting,,,,,,,'
print('string ->', string)

# lstrip, rstrip, strip -> by default, it takes spaces
print('lstrip ->', string.lstrip(','))  # Removes leading commas
print('rstrip ->', string.rstrip(','))  # Removes trailing commas
print('Strip ->', string.strip(','))    # Removes both

print('-' * 75)

# Replace
rep_str = string.strip(',@').replace(',', ' >> ')
print('Replaced String ->', rep_str)
print('Original String ->', string)

print('-' * 75)
