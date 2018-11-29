print('-' * 75)

# Dictionary of Lists
'''
name      location       salary
--------------------------------
justin    pune           7000
davies    orissa         8000
mike      mumbai         9000
'''

emp = {
    'name': [],
    'loc': [],
    'sal': []
}

# Get the input from the user
for cnt in range(1,4):
    name = input('Enter Name ' + str(cnt) + ' -> ')
    loc = input('Enter Location ' + str(cnt) + ' -> ')
    sal = input('Enter Salary ' + str(cnt) + ' -> ')

    # Add the values to the dictionary
    emp['name'].append(name)
    emp['loc'].append(loc)
    emp['sal'].append(sal)

    print('Record ' + str(cnt) + ' Added')

    print('-' * 75)

# Dictionary
for col, value in emp.items():
    print(col, '->', value)

print('-' * 75)

# SELECT * FROM emp WHERE name='value';
while True:
    name = input('Enter name to retrieve the details -> ')
    if not name:
        break

    # Check the existence of user
    if name in emp['name']:
        # Retrieve the index
        idx = emp['name'].index(name)

        # Retrieve loc and sal
        loc = emp['loc'][idx]
        sal = emp['sal'][idx]

        # Display the details
        print(name, loc, sal, sep=' -> ')
    else:
        print("Employee " + name + ' doesn\'t exist')

print('-' * 75)

# UPDATE emp SET loc='value' WHERE name='value';
while True:
    name = input('Enter name to update the location -> ')
    loc = input('Enter new location -> ')
    if not name or not loc:
        break

    # Check the existence of user
    if name in emp['name']:
        # Retrieve the index
        idx = emp['name'].index(name)

        # Update loc
        emp['loc'][idx] = loc

    else:
        print("Employee " + name + ' doesn\'t exist')

print('-' * 75)

# Dictionary
for col, value in emp.items():
    print(col, '->', value)

print('-' * 75)

'''
loc = ['bang', 'che', 'bang', 'che']
'''

# SELECT * FROM emp WHERE loc='value' (Consider it has multiple values)
while True:
    loc = input('Enter loc to retrieve the details -> ')
    if not loc:
        break

    # Check the existence of loc
    if loc in emp['loc']:
        idx = 0
        start_pos = 0
        
        while True:
            try:
                # Retrieve the index
                tmp_idx = emp['loc'][start_pos:].index(loc)
                if start_pos != 0:
                    idx = tmp_idx + start_pos
                else:
                    idx = start_pos

                print('Temp Index ->', tmp_idx)
                print('Index ->', idx)
                print('Start Pos ->', start_pos)

                # Retrieve name and sal
                name = emp['name'][idx]
                sal = emp['sal'][idx]

                # Display the details
                print(name, loc, sal, sep=' -> ')

                # Update Start Position
                start_pos += tmp_idx + 1
            except:
                break
    else:
        print("Location " + loc + ' doesn\'t exist')

print('-' * 75)

