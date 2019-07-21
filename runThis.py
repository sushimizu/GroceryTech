from flask import Flask , render_template
from flask import request

from buyerAccountInfo7 import buyerAccInfo

app = Flask(__name__)

"""Temporary usernames, add SQL queries later"""
def validBuyer(uname, passwd):
	if uname == 'buyer' and passwd == 'b':
		return True
	else:
		return False
	
def validDeliverer(uname, passwd):
	if uname == 'deliverer' and passwd == 'd':
		return True
	else:
		return False
	
def validManager(uname, passwd):
	if uname == 'manager' and passwd == 'm':
		return True
	else:
		return False


@app.route('/', methods=['GET','POST']) 
def index():
	return render_template('login1.html')


@app.route('/registrationType', methods=['GET','POST'])
def registrationType():
	return render_template('registrationType2.html')

@app.route('/delivererFunctionality', methods=['GET','POST'])
def delivererFunctionality():
	return render_template('delivererFunctionality18.html')

@app.route('/managerFunctionality', methods=['GET','POST'])
def managerFunctionality():
	return render_template('managerFunctionality22.html')

"""Will have to change the name of this """
@app.route('/loginReq', methods=['GET','POST'])
def loginReq():
	if request.method == 'POST':
		if validBuyer(request.form['username'], request.form['password']):
			return render_template('buyerFunctionality6.html')
		
		elif validDeliverer(request.form['username'], request.form['password']):
			return render_template('delivererFunctionality18.html')
		
		elif validManager(request.form['username'], request.form['password']):
			return render_template('managerFunctionality22.html')
		
		else:
			
			error="Invalid Username/Password"
			
		
	return render_template('login1.html', error=error)


@app.route('/buyerFunctionality', methods=['GET','POST'])
def buyerFunctionlity():
	return render_template('buyerFunctionality6.html')


@app.route('/registerBuyer', methods=['GET','POST'])
def registerBuyer():
	return render_template('registerBuyer3.html')

@app.route('/registerDeliverer', methods=['GET','POST'])
def registerDeliverer():
	return render_template('registerDeliverer4.html')

@app.route('/registerManager', methods=['GET','POST'])
def registerManager():
	return render_template('registerManager5.html')

@app.route('/storeHomepage', methods=['GET','POST'])
def storeHomepage():
	return render_template('storeHomepage9.html')

@app.route('/buyerAccountInfo', methods=['GET','POST'])
def buyerAccountInfo():
	return buyerAccInfo()



arr = ['Maki', 'Tobin', 'Daniel', 'Oldrin'] 
@app.route('/test', methods=['GET','POST'])
def test():
	"""
	<!doctype html>
	<html>
	<head>
		<link rel="stylesheet" href="/static/style.css"/>
	</head>
	<body>
	<h1><center> Go home </h1></center>
	<section>
	<center><a href='http://0.0.0.0:5000'> Login </a></center>
	</section>
	</body>
	</html>
	"""
	top = """
	<!doctype html>
	<html>
	<head>
		<link rel="stylesheet" href="/static/style.css"/>
	</head>
	<body>
	<h1><center> Go home </h1></center>
	<section>
	<center><a href='http://0.0.0.0:5000'> Login </a></center>
	</section> """
	middle = ""
	for i in range(0,4):
		middle = middle + arr[i] + " " 
	end = """ </body>
	</html>
	"""
	page = top + middle + end
	return page


if __name__ == '__main__' :
	app.run()
