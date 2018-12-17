# Telnet Automation

import telnetlib
from credentials import user, passwd
import os
import time
import re

print('-' * 70)

# Variables
hostname = 'localhost'

try:
    # Connect to Telnet Server
    tn = telnetlib.Telnet(hostname, port=23, timeout=30)
    print('Telnet Connected')

    # Username
    tn.read_until(b"login: ")
    tn.write(user.encode('ascii') + b'\n')
    print('Username Entered')

    # Password
    tn.read_until(b"Password:")
    tn.write(passwd.encode('ascii') + b'\n')
    print('Password Entered')

    print('-' * 70)

    # Execute the script decorators.py
    remote_script_fname = os.path.join(os.getcwd(),
                                       'json_module.py')
    remote_output_file = os.path.join(os.getcwd(),
                                      'remote_dir',
                                      'json_module.log')

    # Change the command prompt
    cmd = b"export PS1='$ '"
    tn.write(cmd + b'\n')

    print('Executing the script ->', remote_script_fname)
    cmd = b"python " + remote_script_fname.encode('ascii') + b' > ' + remote_output_file.encode('ascii')
    cmd = b"ls *.txt > output.txt &\n"
    cmd = b"nohup ls *.txt &\n"
    print(cmd)
    tn.write(cmd + b'\n')
    #time.sleep(10)
    tn.read_until(b"$ ")
    tn.write(b'exit\n')
    print('LOGOUT')

    # Read all the outputs
    print('Reading all the outputs')
    print('-' * 70)
    std_out = tn.read_all().decode('ascii')

    # Read only .txt files
    print('All text files ->', re.findall(r'\b\w+\.txt\b',
                                          std_out))
    print('-' * 70)

    # Close
    tn.close()
    print('Telnet Connection Closed')
except Exception as e:
    print(e.__class__.__name__ + ' -> ' + str(e))

print('-' * 70)

