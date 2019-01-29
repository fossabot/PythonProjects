# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 09:16:40 2019

@author: jmat
"""

from tkinter import *
import random

window=Tk()
def thanos_fn():
    t1.delete("1.0",END)
    x=random.randrange(0,5)
    if x%2==0:
        t1.insert(END,"You were slain by Thanos, for the good of the Universe",END)
    else:
        t1.insert(END,"You were spared by Thanos",END)

b1=Label(window,text="The Decimation Simulator")
b1.grid(row=0,column=0)

e1=Button(window,text="Execute",command=thanos_fn)
e1.grid(row=0, column=2)

t1=Text(window,height=5,width=25)
t1.grid(row=3,column=0)


window.mainloop()
