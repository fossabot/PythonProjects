# Dictionary
# Key - Value Pair
# Keys are unique within the dictionary
# Values can be repeated
# Keys are named indexes

print('-' * 75)

# Define a Dictionary
emp = dict()
emp = {}
print(emp, '->', type(emp))

print('-' * 75)

# Assign values to dictionary
emp = {
    'name':'justin',
    'loc':'pune',
    'salary':6000,
    'name':'davies'
}
print('emp ->', emp)

print('-' * 75)

# Lists of Keys
keys = ['name', 'loc', 'salary', 'loc']
values = ['justin', 'pune', 6000, 7000]

# Zip
emp = dict(zip(keys, values))
print('emp using zip ->', emp, '->', type(emp))

print('-' * 75)

# Access the values from the dictionary
print('Using Index ->', emp['name'])
print('Using get ->', emp.get('name'))

print('-' * 75)

# Get the team from the dictionary
# print('Using Index Team ->', emp['team'])
print('Using get loc ->', emp.get('loc', 'orissa'))
print('Using get Team ->', emp.get('team', 'testing'))
print('emp ->', emp)

print('-' * 75)

# Add/Modify the key-value pairs from the dictionary
if 'salary' not in emp:
    emp['salary'] = 9000

if 'domain' not in emp:
    emp['domain'] = 'telecom'

print('After add/modify ->', emp)

print('-' * 75)

# Update method
# If the key is present, it will modify
# If the key is not present, it will add
other = {
    'salary': 10000,
    'domain': 'investments',
    'team': 'support',
    'project': 'Data Migration'
}
emp.update(other)

print('After emp ->', emp)

print('-' * 75)

# keys -> Retrieves all the keys from the dictionary
print(list(emp.keys()), '->', type(emp.keys()))

for key in emp.keys():
    print(key, '->', emp[key])

print('-' * 75)

# values -> Retrieves all the values from the dictionary
for value in emp.values():
    print(value)

print('-' * 75)

# items -> Retrieves the key-value pair from the dictionary
for item in emp.items():
    print(item)

print('-' * 75)

for key, value in emp.items():
    print(key, '->', value)

print('-' * 75)

# Pop -> Remove the key value pair from the dictionary
rem_elem = emp.pop('project')
print('Removed Element ->', rem_elem)
print('After pop ->', emp)

print('-' * 75)

# Del Function
del emp['salary'], emp['team']
print('After Del ->', emp)

print('-' * 75)

# Convert to list
print('Dict to List ->', list(emp))
print('List of Key Value Pairs ->', list(emp.items()))

print('-' * 75)

# Clear the existing elements
emp.clear()
print('After Clear ->', emp)

print('-' * 75)

'''
name      location       salary
--------------------------------
justin    pune           7000
davies    orissa         8000
mike      mumbai         9000
'''





