# Comprehension

print('-' * 75)

num = int(input('Enter Any Number -> '))
cube_list = []

for n in range(1, num + 1):
    if n % 3 == 0:
        cube_list.append(n ** 3)

print('Cube List ->', cube_list)

print('-' * 75)

# List Comprehension
# [expr iteration <condition>]
cube_list_lc = [(n ** 3, n ** 2) for n in range(1, num + 1) if n % 3 == 0]
print('Cube List Using LC ->', cube_list_lc)

print('-' * 75)

# List of Strings
str_list = input('Enter Strings (Separated by Spaces) -> ').split()
palin_list = [elem for elem in str_list if elem == elem[::-1]]
print('Palin List ->', palin_list)

print('-' * 75)

palin_list = [elem == elem[::-1] for elem in str_list]
print('Palin List ->', palin_list)

print('-' * 75)

len_lc = [elem + ':' + str(len(elem)) for elem in str_list]
print('Length LC ->', len_lc)

print('-' * 75)

# Dictionary Comprehension
# {key: value iteration <condition>}

len_dc = {elem: len(elem) for elem in str_list}
print('Length DC ->', len_dc)

print('-' * 75)

lst = []
# Two Iterations
for x in range(1,3):
    for y in range(x, 4):
        lst.append((x, y))

print('List ->', lst)

print('-' * 75)

lst = [(x, y) for x in range(1,3) for y in range(x, 4)]
print('Using Comprehension ->', lst)

print('-' * 75)

