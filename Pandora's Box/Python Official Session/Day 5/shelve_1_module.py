import shelve

print('-' * 70)

data_file = 'data.shelve'

# Create the file
s = shelve.open(data_file, flag='c')

# Add the data to the file
s['script'] = ['php', 'python', 'perl']
s['version'] = ['5.5', '3.7', '5.8']
s['platform'] = ['unix', 'multi', 'windows']

# Close the file
s.close()

print('File Created Successfully')

print('-' * 70)
