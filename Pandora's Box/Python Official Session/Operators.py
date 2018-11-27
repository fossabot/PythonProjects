# Operators

# to evaluate an expression
# to evaluate the condition

print('-' * 75)

print('Arithmetic Operators')
print('Addition ->', 3 + 2)
print('Subtraction ->', 3 - 2)
print('Multiplication ->', 3 * 2)
print('Division ->', 10 / 3)
print('Modulus ->', 3 % 2)
print('Floor Division ->', 10 // 3)
print('Power ->', 3 ** 2)

print('-' * 75)

print('Assignment Operators')

# =, +=, -=, *=, /=, %=, //=, **=
count = 1
count += 4    # count = count + 4
print('Count ->', count)

print('-' * 75)

print('Bitwise Operators')

'''
& -> Bitwise AND; | -> Bitwise OR; ^ -> Bitwise XOR

num1 = 5 -> 0000 0101
num2 = 7 -> 0000 0111
&        -> 0000 0101
|        -> 0000 0111
^        -> 0000 0010
'''
print('Decode ->', type(b'0000 0101'.decode()))
print('Bitwise AND ->', 5 & 7)
print('Bitwise OR  ->', 5 | 7)
print('Bitwise XOR ->', 5 ^ 7)

print('-' * 75)

# Left Shift and Right Shift

'''
5 << 2 (left shift)
0000 0101
0000 1010
0001 0100 => 20

5 >> 2 (right shift)
0000 0101
0000 0010
0000 0001 => 1
'''
print('Left Shift 5 twice ->', 5 << 2)
print('Right Shift 5 twice ->', 5 >> 2)

print('-' * 75)

# Comparison Operators
# ==, !=, >, <, >=, <=
print('php greater than perl ->', 'php' > 'perl')
print('Is php palindrome ->', 'php' == 'php'[::-1])

print('-' * 75)

# Logical comparison operators
# and => True when all the conditions are satisfied
# or => True when any of the given conditions are satisfied
# not => Inverts the result of the conditional expression
string = 'php'
print('Using and ->', len(string) % 2 == 0 and string == string[::-1])
print('Using or ->', len(string) % 2 == 0 or string == string[::-1])
print('Using not ->', not(len(string) % 2 == 0 and string == string[::-1]))

print('-' * 75)

# Membership Operators (in, not in)
string = 'python scripting'
chk_string = 'on'
print('Is on present ->', chk_string in string)

print('-' * 75)

# Concatenation (+)
# All the operands should be of same type and the type should not be int
print('Concat 1 ->', 2 + 3)
print('Concat 2 ->', '2' + '3')
print('Concat 3 ->', '2' + ' ' + str(3))

print('-' * 75)


