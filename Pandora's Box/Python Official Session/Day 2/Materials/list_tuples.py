# List of Tuples

print('-' * 75)

lst_of_tup = [('php', 'v5.5'),
              ('perl', 'v5.8')]
print('List of Tuples ->', lst_of_tup)

print('-' * 75)

lst_of_tup.append(('python', 'v3.7.1'))

for elem in lst_of_tup:
    print(elem, '->', type(elem))

print('-' * 75)

# Tuple of Lists
tup_of_lst = (['php', 'perl'],
              ['v5.5', 'v5.8'])
#tup_of_lst[0].clear()
#tup_of_lst[0][0] = 5
print('Tuple of Lists ->', tup_of_lst)

print('-' * 75)

tup_of_lst[0].append('python')
tup_of_lst[1].append('v3.7.1')

for elem in tup_of_lst:
    print(elem, '->', type(elem))

print('-' * 75)

# Shallow Copy and Deep Copy
lst_a = ['python']

# Shallow Copy -> Both will be having the same reference
# Changing 'A' -> 'B' will also be impacted
# Changing 'B' -> 'A' will also be impacted
lst_b = lst_a

print('Shallow -> ID of A ->', id(lst_a))
print('Shallow -> ID of B ->', id(lst_b))

# Deep Copy -> Only values will be copied, not the reference
lst_b = lst_a[:]

print('Deep -> ID of A ->', id(lst_a))
print('Deep -> ID of B ->', id(lst_b))

print('List A ->', lst_a)
print('List B ->', lst_b)

# Change list A
lst_a.append('php')
print('Modify A -> List A ->', lst_a)
print('Modify A -> List B ->', lst_b)

# Change list B
lst_b.append('perl')
print('Modify B -> List A ->', lst_a)
print('Modify B -> List B ->', lst_b)

print('-' * 75)

