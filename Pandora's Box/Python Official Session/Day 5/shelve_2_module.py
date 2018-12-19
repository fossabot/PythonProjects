import shelve

print('-' * 70)

data_file = 'data.shelve'
data = shelve.open(data_file, flag='r')
print('Data ->', data)

for col, value in data.items():
    print(col, '->', value)

data.close()

print('-' * 70)
