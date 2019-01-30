# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:49:30 2019

@author: jmat
"""

import psychopg2

def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT , quantity INTEGER,  price REAL )")
    cur.execute("INSERT INTO store VALUES ( 'Wine Glass',8,10.5)  ")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)", (item,quantity,price))
    conn.commit()
    conn.close()
    
def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

#conn=sqlite3.connect("lite.db")
#cur=conn.cursor()
#conn.close()
delete('Coffee Glass')
print(view())

