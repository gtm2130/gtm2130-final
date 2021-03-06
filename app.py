#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 04:00:32 2020

@author: gabrielmccormick
"""
#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/colors")
def colors():
    return render_template("index2.html")

@app.route("/animals")
def animals():
    return render_template("index3.html")


#start the server
if __name__ == "__main__":
    app.run()