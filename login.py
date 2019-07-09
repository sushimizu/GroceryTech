#!/usr/bin/python

import cgi
import requests 
import webbrowser

print "Content-type: text/html\n\n"
	print ""
	print """
	<!doctype html>
	<html>
	<style>
	h1{
		color: black;
	}
	</style>
	<html>
	<head>
		<title>Buyer Functionality</title>
		<link rel="stylesheet" type="text/css" href="./style.css"/>
	</head>
<body>

	
	<h2> Buyer Functionality</h2>
	
		
		<form action="listOfStores8.html">
	  <input type="submit" value="New Order"> <br> <br>
		</form>
		<form >
	  <input type="submit" value="Order History"> <br> <br>
		</form>
		<form action="buyerAccountInfo7.html">
	  <input type="submit" value="Account Information"> <br> <br>
		</form>
    <form >
	  <input type="submit" value="Payment Information"> <br> <br>
		</form>
		<form action="login1.html">
	  <input type="submit" value="Logout" >
		</form>
	

</body>
	</html>
	"""



webbrowser.open("buyerFunctionality6.html")
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
