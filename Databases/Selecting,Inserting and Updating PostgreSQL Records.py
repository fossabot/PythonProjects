# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:49:30 2019

@author: jmat
"""

import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='1234' host='localhost' port='5432'" )
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT , quantity INTEGER,  price REAL )")
    #cur.execute("INSERT INTO store VALUES ( 'Wine Glass',8,10.5)  ")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='1234' host='localhost' port='5432'" )
    cur=conn.cursor()
#   cur.execute("INSERT INTO store VALUES ('%s','%s','%s')" % (item,quantity,price) ) 
## Above statement is Vulnerable to SQL Injection
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item,quantity,price) )  

    conn.commit()
    conn.close()
    
def view():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='1234' host='localhost' port='5432'" )
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='1234' host='localhost' port='5432'" )
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='1234' host='localhost' port='5432'" )
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity= %s ,price=%s WHERE item=%s", (quantity,price,item))
    conn.commit()
    conn.close()

create_table()

insert("Coffee Cup",12,6.5)
#print( view() )

#delete("Coffee Cup")
#print( view() )

print( view() )
update(20,15,"Coffee Cup")
print( view() )