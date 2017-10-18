# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 22:12:57 2017

@author: 5004756
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(port=5000, debug=True)