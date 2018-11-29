print('-' * 75)

# Dictionary of Lists
'''
name      location       salary
--------------------------------
justin    pune           7000
davies    orissa         8000
mike      mumbai         9000

{
    'justin': {
                'loc': 'pune',
                'sal': 7000
              },
    'davies': {
                'loc': 'orissa',
                'sal': 8000
              }
}
'''

emp = {}

# Get the input from the user
for cnt in range(1,4):
    name = input('Enter Name ' + str(cnt) + ' -> ')
    loc = input('Enter Location ' + str(cnt) + ' -> ')
    sal = input('Enter Salary ' + str(cnt) + ' -> ')

    # Add the values to the dictionary
    emp[name] = {'loc': loc, 'sal': sal}
    print('Record ' + str(cnt) + ' Added')

    print('-' * 75)

# Dictionary
for col, value in emp.items():
    print(col, '->', value)

print('-' * 75)

# SELECT * FROM emp WHERE name='value'
while True:
    name = input('Enter Name -> ')

    if not name:
        break

    # Check for the existence
    if name in emp:
        print('Name ->', name)
        print('Location ->', emp[name]['loc'])
        print('Salary ->', emp[name].get('sal'))
    else:
        print(name + ' Not Found')

    print('-' * 75)

print('-' * 75)

