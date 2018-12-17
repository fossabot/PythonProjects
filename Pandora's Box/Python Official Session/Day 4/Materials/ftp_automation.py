# FTP Automation

print('-' * 70)

import ftplib as ftp
import getpass
import glob
import os
import sys

# Connect
try:
    conn = ftp.FTP('127.0.0.1')
except Exception as e:
    print(e.__class__.__name__ + ' -> ' + str(e))
    print('-' * 70)
    sys.exit()
else:
    print('Connected to FTP ->', conn)

# Authentication
conn.login(user=getpass.getuser(),
           passwd=getpass.getpass())

print('Files ->', conn.dir())
print('Login Successful')

print('-' * 70)

# Directories and Files
ldir = os.path.join(os.getcwd(), 'local_dir')
rdir = os.path.join(os.getcwd(), 'remote_dir')
rfname = os.path.join(rdir, 'remote_file.py')
lfname = os.path.join(ldir, 'from_remote_serevr.py')

# Loop through the local_dir
for fname in glob.glob(ldir + '/*'):
    print('Filename ->', fname)

    # Transfer the file to the ftp server
    conn.storbinary('STOR ' + rfname, open(fname, 'rb'))

print('-' * 70)

# Get the file from the remote server
localfname = open(lfname, 'wb')
conn.retrbinary('RETR ' + rfname, localfname.write, 1024)
localfname.close()
print('File Retrived')

print('-' * 70)

# Close the connection
conn.close()
print('Connection Closed')

print('-' * 70)
