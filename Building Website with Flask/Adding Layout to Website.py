# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 06:57:41 2019

@author: jmat
"""

from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home_extend.html")


@app.route('/about/')
def about():
    return render_template("about_extends.html")

if __name__=="__main__":
    app.run(debug=True)