# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 06:31:52 2019

@author: jmat
"""

from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "Website content goes here!"

if __name__=="__main__":
    app.run(debug=True)