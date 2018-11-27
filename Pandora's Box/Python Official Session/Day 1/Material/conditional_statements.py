# Conditional Statements

print('-' * 75)

# Simple IF ELSE
# Statements within the block should follow the same indentation level
# Statement across the blocks can follow any levels of indentation
if False:
    print('Statement 1')
    print('Statement 2')
    print('Statement 3')
else:
    print('Statement 4')
    print('Statement 5')

print('-' * 75)

# Ternary form of IF ELSE
string = '123212'
chk_palin = True if string == string[::-1] else False
print('Check Palin ->', chk_palin)

print('-' * 75)

# Multilevel IF ELSE (Alternative to SWITCH CASE statements)
num = 29

if num % 5 == 0:
    print('Divisible by 5')
elif num % 3 == 0:
    print('Divisible by 3')
elif num % 2 == 0:
    print('Divisible by 2')
else:
    print('Not Divisible by 5, 3 and 2')

print('-' * 75)

# Nested IF ELSE
num = 121

if num % 5 == 0:
    print('Divisible by 5')

    if num % 3 == 0:
        print('Divisible by 3')

        if num % 2 == 0:
            print('Divisible by 2')
        else:
            print('Not Divisible by 2')
    else:
        print('Not Divisible by 3')
else:
    print('Not Divisible by 5')

print('-' * 75)

