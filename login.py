#!/usr/bin/python

import cgi
import requests 
import webbrowser


r = requests.post("login1.html", data={'username','password'})
#print (r.text)
if data['username'] == 'buyer' :
	webbrowser.open("buyerFunctionality6.html")
else :
	webbrowser.open("login1.html")
	


#form = cgi.FieldStorage()

"""
try:
	#catch username 
	uname = form['username'].value
	url = form['URL'].value
except KeyError as E:
	pass
""" 
"""
if form.getvalue("username"): 
	uname = form.getvalue("username")
if form.getvalue("password"): 
	pwd = form.getvalue("password")
	

  
uname, pwd = map(String, uname.split(',')) 

f = open("usernamePwd.csv","rb")
f.write(uname; pwd) 
f.close() 

 """	
