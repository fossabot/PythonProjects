import pickle

# Data
data = {
    'name': 'justin',
    'location': 'bangalore',
    'salary': 5000,
    'domain': 'telecom',
    'project': 'support'
}

# Write the data
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

print('Pickle File Created')

print('-' * 70)

# Load the data
with open('data.pickle', 'rb') as f:
    data = pickle.load(f)
    print(data)

print('-' * 70)
