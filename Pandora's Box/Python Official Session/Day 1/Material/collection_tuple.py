# tuple
# Immutable
# Constant Lists

print('-' * 75)

# Definition of tuple
num_tuple = ()
num_tuple = tuple()
print(num_tuple, '->', type(num_tuple))

# Using concatenation ops
num_tuple = tuple(range(1,6)) + tuple(range(10,5,-1))
print('num_tuple ->', num_tuple)

# Using repetition ops
# tuple(range(1, 6, 2)) => (1, 3, 5)
# tuple(range(1, 6, 2))[1:] => (3, 5)
# tuple(range(1, 6, 2))[1:] * 2 => (3, 5, 3, 5)

rep_tuple = tuple(range(1, 6, 2))[1:] * 2
print('rep_tuple ->', rep_tuple)

# Hard coding the values
scr_tuple = ('php', 'perl', 'python', 'ruby', 'shell', 'vbscript')
print('scr_tuple ->', scr_tuple)

# Using Indexing and Slicing
mixed_tuple = (scr_tuple[2],
              scr_tuple[-3:],
              scr_tuple[-3::-1])
print('Mixed tuple ->', mixed_tuple)

print('-' * 75)

# Accessing the element within the nested tuple
print('2nd Element ->', mixed_tuple[1], '->', type(mixed_tuple[1]))
print('Last Element in the 2nd Index ->', mixed_tuple[1][-1])

print('-' * 75)

# Membership Operator
print('Is on present in scr_tuple ->', 'on' in scr_tuple)
print('Is php present in scr_tuple ->', 'php' in scr_tuple)

print('-' * 75)

# Functions
# Len => can apply on tuples that contains any type of elements
print('Length ->', len(mixed_tuple))

# Max, Min, Sorted => can apply on tuples that contains same type of elements
print('Max ->', max(scr_tuple))
print('Min ->', min(scr_tuple))
print('Sorted ->', tuple(sorted(scr_tuple)))   # Ascending Order
print('Reverse Order of Sorted ->', sorted(scr_tuple, reverse=True)) # Descending

# Sum => Can apply on tuples that contains only integers
print('Sum ->', sum(num_tuple))

print('-' * 75)

# Common methods

# Count
print('No: of php ->', scr_tuple.count('php'))

# Index
print('Index of php ->', scr_tuple.index('php'))

print('-' * 75)



