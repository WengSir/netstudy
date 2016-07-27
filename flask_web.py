#!/bin/env python
#encoding:utf-8

import MySQLdb as mysql
import json
from flask import Flask, request, render_template
app = Flask(__name__)
db = mysql.connect(host='192.168.16.63',user="root", passwd="zdsoft", db="falcon", charset="utf8")
db.autocommit(True)
cur = db.cursor()

@app.route('/')
def index():
	return render_template('monitor.html')

if __name__ == "__main__":
	app.run(host="0.0.0.0",port=8181,debug=True)


