import shelve

print('-' * 70)

# Data File
data_file = 'data.shelve'

# Open the data for updating
data = shelve.open(data_file, flag='w', writeback=True)

# Add the records
data['script'].append('C#')
data['version'].append('12.34')
data['platform'].append('windows')
data.sync()
print('C# Added')

# Update the value
script = input('Enter name of the script -> ')
version = input('Enter the version to update -> ')
if script in data['script']:
    idx = data['script'].index(script)
    data['version'][idx] = version
else:
    print('{} not found'.format(script))

data.sync()
print('Version Updated')

# Update the value
script = input('Enter name of the script -> ')
if script in data['script']:
    idx = data['script'].index(script)

    for col in data:
        data[col].pop(idx)
else:
    print('{} not found'.format(script))

data.sync()
print('Script Deleted')

# Close the file
data.close()

print('-' * 70)
