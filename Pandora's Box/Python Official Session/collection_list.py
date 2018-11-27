# List

print('-' * 75)

# Definition of List
num_list = []
num_list = list()
print(num_list, '->', type(num_list))

# Using concatenation ops
num_list = list(range(1,6)) + list(range(10,5,-1))
print('num_list ->', num_list)

# Using repetition ops
# list(range(1, 6, 2)) => [1, 3, 5]
# list(range(1, 6, 2))[1:] => [3, 5]
# list(range(1, 6, 2))[1:] * 2 => [3, 5, 3, 5]

rep_list = list(range(1, 6, 2))[1:] * 2
print('rep_list ->', rep_list)

# Hard coding the values
scr_list = ['php', 'perl', 'python', 'ruby', 'shell', 'vbscript']
print('scr_list ->', scr_list)

# Using Indexing and Slicing
mixed_list = [scr_list[2],
              scr_list[-3:],
              scr_list[-3::-1]]
print('Mixed List ->', mixed_list)

print('-' * 75)

# Accessing the element within the nested list
print('2nd Element ->', mixed_list[1], '->', type(mixed_list[1]))
print('Last Element in the 2nd Index ->', mixed_list[1][-1])

print('-' * 75)

# Membership Operator
print('Is on present in scr_list ->', 'on' in scr_list)
print('Is php present in scr_list ->', 'php' in scr_list)

print('-' * 75)

# Functions
# Len => can apply on lists that contains any type of elements
print('Length ->', len(mixed_list))

# Max, Min, Sorted => can apply on lists that contains same type of elements
print('Max ->', max(scr_list))
print('Min ->', min(scr_list))
print('Sorted ->', sorted(scr_list))    # Ascending Order
print('Reverse Order of Sorted ->', sorted(scr_list, reverse=True)) # Descending

# Sum => Can apply on lists that contains only integers
print('Sum ->', sum(num_list))

print('-' * 75)

# Common methods

# Count
print('No: of php ->', scr_list.count('php'))

# Index
print('Index of php ->', scr_list.index('php'))

print('-' * 75)



