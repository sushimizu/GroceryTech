from flask import Flask , render_template
from flask import request
import db

from buyerAccountInfo7 import buyerAccInfo

app = Flask(__name__)
currentUser = ""
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


"""Will have to change the name of this """
@app.route('/loginReq', methods=['GET','POST'])
def loginReq():
	if request.method == 'POST':
		_name = request.form['username']
		_password = request.form['password']
		num = db.login(_name, _password)
		global currentUser
		if num == 1:
			currentUser = _name
			return render_template('managerFunctionality22.html')
		elif num == 2:
			currentUser = _name
			return render_template('delivererFunctionality18.html')
		elif num == 3:
			currentUser = _name
			return render_template('buyerFunctionality6.html')
		else:
			return render_template("login1.html", error="Credentials Incorrect")

@app.route("/login")
def login():

	error="Invalid Username/Password"

	return render_template('login1.html', error=error)


@app.route('/buyerFunctionality', methods=['GET','POST'])
def buyerFunctionlity():
	return render_template('buyerFunctionality6.html')


@app.route('/registerBuyer', methods=['GET','POST'])
def registerBuyer():

	if request.method == "POST":
		fname = request.form['fname']
		uname = request.form['uname']
		password = request.form['password']
		email = request.form['email']
		street = request.form['street']
		houseNo = request.form['houseNo']
		city = request.form['city']
		lname = request.form['lname']
		phone = request.form['phone']
		cpassword = request.form['cpassword']
		state = request.form['state']
		zip = request.form['zip']

		error1 = "your password is messed up bro"
		error2 = "phone has incorrect number of digits"
		error3 = "zip code has incorrect number of digits"
		error4 = "email contains non-alphanumeric characters"
		if password != cpassword:
			return render_template("registerBuyer3.html", error=error1)
		if (len(str(abs(phone)))) != 10:
			return render_template("registerBuyer3.html", error=error2)
		if (len(str(abs(zip)))) != 5:
			return render_template("registerBuyer3.html", error=error3)
		a, b, c = email.rsplit('@', '.')
		if a.isalnum() and b.isalnum() and c.isalnum():
			return render_template("registerBuyer3.html", error=error4)





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


@app.route('/findItem', methods=['GET','POST'])
def findItem():
	return render_template('findItem10.html')




if __name__ == '__main__' :
	app.run()
