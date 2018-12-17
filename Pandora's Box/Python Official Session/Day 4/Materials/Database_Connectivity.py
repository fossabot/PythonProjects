# Database Connectivity

'''
emp_id, emp_name, emp_project
1, davies, development
2, tris, testing
1, davies, testing

emp - table 1
emp_id
emp_name

emp_project - table 2
emp_id,
emp_proj_name

table1 (emp):
emp_id     emp_name
1          davies
2          tris

table2 (emp_project)
emp_id     emp_proj_name
1          development
2          testing
1          testing

a) Import the specific module
   pymysql - MySQL
   cx_Oracle - Oracle
   psycopg2 - PostgreSQL
   ibm_db - DB2
   pymssql - MS SQL Server
   pyodbc - All databases (Requires Database Driver)

b) Documentation - http://docs.python.org/3

c) Install a Module - pymysql
   1) Go to the Python Installable Path
      Change to 'Scripts' Directory
      Execute the command 'pip install pymysql'
      Install all dependant modules automatically

    2) Go to the URL 'http://pypi.org'
       Search for the project 'pymysql'
       Click on the Latest Version
       Click 'Download Files'
       Click 'whl' file that supports Platform and Python Version
       Exec the command 'pip install <whl_file_name>'

    3) Same as 4 steps in approach 2
       Click '.tar.gz' file to download
       gunzip the file using any supported software
       untar the file '*.tar'
       Open the command prompt
       Go to the directory where it is tarr'ed
       python setup.py install

    The dependant modules needs to be installed
    explicitly for approaches (2) and (3)

d) Import the module - pymysql

e) Create the database connection which returns the
   connection object

f) Create the database cursor using the connection object
   which returns the cursor object

g) Form the SQL

h) Execute the SQL using the cursor object

i) For DML Queries (INSERT, UPDATE and DELETE), user can
   commit or rollback depends on the req

j) For SELECT statements, retrieve the recordset using the
   cursor object
   fetchone - retrieves one record at a time
   fetchmany(n) - retrieves 'n' records at a time
   fetchall - retrieves all the records at once

k) Process the data

l) Close the database cursor object

m) Close the database connection object
'''

print('-' * 70)

import pymysql as db
import getpass
import sys

# Connect
try:
    conn = db.connect('localhost',
                      'root',
                      getpass.getpass(),
                      'employee')
except Exception as e:
    print(e.__class__.__name__ + ' -> ' + str(e))
    print('-' * 70)
    sys.exit()

print('Database connection Successful')

# Database Cursor
cursor = conn.cursor()
print('Database cursor created')

print('-' * 70)

sql = '''INSERT INTO emp_details(name, location)
VALUES('{}', '{}')
'''.format('ravi', 'mysore')
cursor.execute(sql)
conn.commit()
print('Data Inserted')

print('-' * 70)

sql = 'SELECT id, name, location FROM emp_details'
cursor.execute(sql)
print('Query Executed')

print('Number of Records ->', cursor.rowcount)

print('-' * 70)

# Fetchone
print('Fetchone ->', cursor.fetchone())

print('-' * 70)

# Fetchmany
print('Fetchmany ->', cursor.fetchmany((5)))

print('-' * 70)

# Fetchall
print('Fetchall ->', cursor.fetchall())

print('-' * 70)

conn.close()
print('Connection Done')

print('-' * 70)
