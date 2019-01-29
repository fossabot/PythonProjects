# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 19:20:41 2019

@author: jmat
"""

from tkinter import *

window=Tk()

b1=Button(window,text="Subscribe to PewdiePie")

#Either use pack or grid function to add the button to main window
#b1.pack()
b1.grid(row=0,column=0)
#b1.grid(row=0,column=0,rowspan=2)


e1=Entry(window)
e1.grid(row=0, column=1)

#t1=Text(window)
t1=Text(window,height=2,width=20)
t1.grid(row=0,column=2)
window.mainloop()