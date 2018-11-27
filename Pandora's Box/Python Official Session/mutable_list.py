# List is Mutable

print('-' * 75)

# List
scr_list = ['php', 'perl', 'python', 'ruby', 'shell', 'vbscript']
print('scr_list ->', scr_list)

print('-' * 75)

# Modifying the existing element in the list
scr_list[-1] = 'javascript'
print('After Modify idx -1 =>', scr_list)

scr_list[2:4] = ['php', 'java']
print('After Modify 2 ->', scr_list)

scr_list[2:4] = ['perl']
print('After Modify 3 ->', scr_list)

print('-' * 75)

# Adding the elements to the list

# Append -> always adds the given element to the end of the list
ret = scr_list.append('perl')
print('After Append ->', scr_list)
print('Ret ->', ret)

# Insert -> inserts the given element in the given position
scr_list.insert(0, 'perl')
print('After Insert ->', scr_list)

# Extend -> adds the elements from the iterable object to the end of list
other = ['perl', 'php', 'perl', 'python']
scr_list.extend(other)  # scr_list = scr_list + other
print('After Extend ->', scr_list)

scr_list.append(other)
print('After Append ->', scr_list)

print('-' * 75)

final_list = scr_list[:4] + other + scr_list[4:]
print('Final List ->', final_list)

print('-' * 75)

ins_pos = [3, 2, 9]
for pos in ins_pos:
    scr_list.insert(pos, 'C')

scr_list.insert(100,'C')
print('scr_list ->', scr_list)

print('-' * 75)

# Removing the elements from the list
# pop
rem_elem = scr_list.pop() # By default, it removes the last element in the list
print('Removed Element ->', rem_elem)
print('After Pop 1 ->', scr_list)

print('-' * 75)

rem_elem = scr_list.pop() # By default, it removes the last element in the list
print('Removed Element ->', rem_elem)
print('After Pop 2 ->', scr_list)

print('-' * 75)

rem_elem = scr_list.pop(-3)
print('Removed Element ->', rem_elem)
print('After Pop 3 ->', scr_list)

print('-' * 75)

# remove
scr_list.remove('perl')
print('After Remove 1 ->', scr_list)

while scr_list.count('perl'):
    scr_list.remove('perl')
else:
    print('All occurrences of perl has been removed')

print('After Remove All ->', scr_list)

print('-' * 75)

# Del -> deleting the object
del scr_list[1:4]
# del scr_list
print('After Del ->', scr_list)

print('-' * 75)

# Empty the list
scr_list.clear()    # del scr_list[:]
print('After Clear ->', scr_list)

print('-' * 75)



