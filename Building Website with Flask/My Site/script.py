# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 06:31:52 2019

@author: jmat
"""

from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "This is my Homepage"


@app.route('/about/')
def about():
    return "Simple Website using Python and Flask!"

if __name__=="__main__":
    app.run(debug=True)