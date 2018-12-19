# SSH - Secure Shell

'''
Public Keys and Private Keys
PuttyKeyGen

Local Server - Private Key
Remote Server 1 - Public Key
Remote Server 2 - Public Key
'''

import paramiko

print('-' * 70)

# SSH Client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print('Created Client and Added Policy')

# Make connection and create shell
client.connect('localhost', 22, 'kanish', 'pass123')
shell = client.invoke_shell()
print('Connection Made and Created Shell')

# Execute the command and get the results
ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command('ls *.date')
for line in ssh_stdout.readlines():
    print('ssh_stdout - {}'.format(line), end='')

print('Standard Error ->', ssh_stderr.read())

print('-' * 70)

cmd = 'find /Users/kanish/Training/Cypress_Python_Dec2018/ -name "*.py" | xargs grep -l "import paramiko"'
ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command(cmd)
for line in ssh_stdout.readlines():
    print('ssh_stdout - {}'.format(line), end='')

print('-' * 70)

# Closing the connection
ssh_stdout.close()
ssh_stderr.close()
ssh_stdin.close()
shell.close()
client.close()
print('Connection Closed')

print('-' * 70)
