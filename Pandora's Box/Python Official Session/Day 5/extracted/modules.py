import os
import sys
import datetime
import re

print('-' * 50)

# Read all the environmental variables
for env, value in os.environ.items():
    print(env, '->', value)

print('-' * 50)

print('PYTHONPATH ->', os.environ['PYTHONPATH'])

print('-' * 50)

# Current working directory
dir_name = os.getcwd()
print('Directory ->', dir_name)

print('-' * 50)

# List the contents of the directory
for attr in os.listdir(dir_name):
    if os.path.isdir(attr):
        print(attr, '-> Directory')

    if os.path.isfile(attr):
        print(attr, '-> File')

print('-' * 50)

# Check for the existence
print('Existence 1 ->', os.path.exists(dir_name))
print('Existence 2 ->', os.access(dir_name, os.F_OK))

print('-' * 50)

# Check for the permissions
print('Read ->', os.access(dir_name, os.R_OK))
print('Write ->', os.access(dir_name, os.W_OK))
print('Execute ->', os.access(dir_name, os.X_OK))

print('-' * 50)

# Basename and Dirname
basename = os.path.basename(dir_name)
print('Basename ->', basename)

dirname = os.path.dirname(dir_name)
print('Dirname ->', dirname)

print('-' * 50)

print('Join 1 ->', os.path.join('dir1', 'dir2', 'dir3'))
print('Join 2 ->', os.path.join(dirname, basename))

print('-' * 50)

# walk
for base, dnames, fnames in os.walk(dirname):
    print('Base Dir ->', base)
    print('Dir Names ->', dnames)
    print('File Names ->', fnames)

    print('-' * 50)

# Get only .py files
for base, dnames, fnames in os.walk(dirname):
    for fname in fnames:
        if fname.endswith('.py'):
            print(os.path.join(base, fname))

print('-' * 50)

# Command Line Arguments
# Arguments that are passed during the runtime
# It is used for Automation
print('All the Arguments ->', sys.argv)

print('-' * 50)

# Filename
print('Only Filename ->', sys.argv[0])

for arg in sys.argv[1:]:
    print('Arg ->', arg)

print('-' * 50)

# Datetime
dt_time = datetime.datetime.now()
print('Current Date and Time ->', dt_time)

today = datetime.date.today()
print('Current Date ->', today)

print('-' * 50)

# Format Specifiers
print('Year ->', dt_time.strftime('%Y - %y'))
print('Month ->', dt_time.strftime('%B - %b - %m'))
print('Day ->', dt_time.strftime('%A - %a - %d'))
print('24 Hour Format ->', dt_time.strftime('%H:%M:%S'))
print('12 Hour Format ->', dt_time.strftime('%I:%M:%S %p'))
print('Week ->', dt_time.strftime('%W - %w'))
print('Number of Days ->', dt_time.strftime('%j'))

print('-' * 50)

print('150 Days from Now ->', dt_time + datetime.timedelta(days=150))
print('3 Weeks from Now ->', dt_time + datetime.timedelta(weeks=3))

print('-' * 50)

# User defined date and time
dt = datetime.datetime(2005, 5, 20, 9, 10, 5)
print('Date ->', dt)
print('Year ->', dt.year)
print('Month ->', dt.month)

print('-' * 50)

# How many days to new year 2019
dt = datetime.date.today()
new_year = datetime.date(dt.year + 1, 1, 1)

print('Current Date ->', dt)
print('New Year 2019 ->', new_year)

if new_year > dt:
    print('No: of Days to go ->', (new_year - dt).days)

print('-' * 50)

print('Dir ->', dir(os))

print('-' * 50)

print(re.search.__doc__)

print('-' * 50)
