import random

print('-' * 70)

# randrange
print('randrange 1 ->', random.randrange(1000))
print('randrange 2 ->', random.randrange(10, 50, 10))
print('randrange 3 ->', random.randrange(1000, 499, -50))

print('-' * 70)

# randint
for n in range(1, 6):
    print('Random {} -> {}'.format(n,
                                   random.randint(1, 10)))

print('-' * 70)

# Choice
print('Choice 1 ->', random.choice(range(1, 100)))
print('Choice 2 ->', random.choice('python php perl'.split()))
print('Choice 3 ->', random.choice('python php perl'))

print('-' * 70)

# Shuffle
lst = list(range(1,6))
random.shuffle(lst)
print('Shuffle ->', lst)

print('-' * 70)

# Sample
print('Sample ->', random.sample('python', 3))

print('-' * 70)

# Uniform
print('Uniform ->', round(random.uniform(100, 501), 3))

print('-' * 70)
