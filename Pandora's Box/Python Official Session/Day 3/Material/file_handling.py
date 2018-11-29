# File Handling

print('-' * 75)

'''
expandtabs - translate tabs to spaces
splitlines - split based on \n
'''

# Primary Modes - r(read mode - default), w(overwritten mode) and a(append mode)

# Function to implement w and a modes
def write_file(fname, fmode):
    # Open the file
    fhandle = open(fname, fmode)

    # Get the input from the user
    while True:
        line = input('Enter a Line -> ')
        if line.lower() == 'eof':
            break

        # Write the contents to the file
        fhandle.write(line + '\n')

    # Close the file
    fhandle.close()

    # Check whether the file is closed
    print('Checking for Closing the file ->', fhandle.closed)

# Filename
data_fname = '/Users/kanish/Training/Cypress_Python_Nov2018/Day_3_29Nov2018/data.txt'

# 'w' mode
# write_file(data_fname, 'w')
print('File Created Successfully')

print('-' * 75)

# 'a' mode
# write_file(data_fname, 'a')
print('Contents Appended Successfully')

print('-' * 75)

# Use of 'with' block using read mode
with open(data_fname) as fread:
    # read => based on the number of characters, it will read the file
    print('Read 1 ->', fread.read(10))
    print('Read 2 ->', fread.read(20))
    print('Read 3 ->', fread.read())
    print('Read 4 ->', fread.read())

    # seek -> Move the cursor to the beginning of the file
    fread.seek(0)
    print('Position ->', fread.tell())

    print('-' * 75)

    '''
    while True:
        line = fread.readline()
        if not line:
            break

        print('Line ->', line.strip('\n'))
    '''
    
    # readline => based on the number of lines, it will be read
    print('Readline 1 ->', fread.readline(10))
    print('Readline 2 ->', fread.readline(20))
    print('Readline 3 ->', fread.readline())

    # seek -> Move the cursor to the beginning of the file
    fread.seek(0)
    print('Position ->', fread.tell())

    print('-' * 75)

    # readlines => To read all the lines in the form of list
    all_lines = fread.readlines()
    print('All Lines ->', all_lines)

    all_lines.insert(4, 'I am new\n')

print('-' * 75)

# Writelines
fwrite = open('data_copied.txt', 'w')
fwrite.writelines(all_lines)
fwrite.close()

print('-' * 75)



