print('-' * 70)

import zipfile
import os

# Directory
dir_name = os.getcwd()

# Create the zip file
with zipfile.ZipFile('all_python_scripts.zip', 'w') as zfname:
    for base, dnames, fnames in os.walk(os.path.dirname(dir_name)):
        for fname in fnames:
            if fname.endswith('.py'):
                print('Zipping the file ->', fname)
                zfname.write(os.path.join(base, fname),
                             arcname=fname)

print('All Python Scripts Zipped Successfully')

print('-' * 70)

# Extract dir
extracted = os.path.join(dir_name, 'extracted')
if not os.path.exists(extracted):
    os.mkdir(extracted)

# Changing the working directory to extracted
os.chdir(extracted)

# Extract the files
zip_fname = os.path.join(dir_name, 'all_python_scripts.zip')
with zipfile.ZipFile(zip_fname, 'r') as zfname:
    zfname.extractall()

print('Contents Extracted')

print('-' * 70)