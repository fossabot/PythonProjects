# Iterators

'''
for => should be used when the set of statements needs to be iterated
       based on a collection (set of values)
       Will not lead to infinite loop

while => should be used when the set of statements needs to be iterated
         based on a condition
'''

print('-' * 75)

# For Loop with Strings and use of break
for ch in 'python':
    if ch == 'a':
        break
    
    print('ch ->', ch)
else:
    print('For Loop DONE')

print('-' * 75)

# For loop with continue
for ch in 'python':
    if ch in ['t', 'o']:     # if ch == 't' or ch == 'o':
        continue
    
    print('ch ->', ch)
else:
    print('For Loop DONE')

print('-' * 75)

# Pass
# Used to define the empty block
num = 1
if num % 1 == 0:
    pass
    print('After Pass')

print('-' * 75)

# Range
# range(n) => 0, 1, 2, 3, 4, 5, ...., n-1
# range(1,n) => 1, 2, 3, 4, 5, ...., n-1
# range(1,n,s) => 1, 1+s, 1+2s, ...., n-1
for n in range(10,5,-1):
    print('Number ->', n)

print('-' * 75)

count = 10
while count > 5:
    print('count ->', count)
    count -= 1
else:
    print('While Loop Done')

print('-' * 75)

# No need to have ELSE block for an infinite loop
while True:
    print('count ->', count)
    count -= 1

    if count < 0:
        break

print('-' * 75)

nums = range(1,6,2)
print(nums, '->', type(nums))

print('-' * 75)

nums = list(range(1,6,2))
print(nums, '->', type(nums))

print('-' * 75)


