from flask import Flask , render_template
from flask import request
import db
import re


app = Flask(__name__)
currentUser = ""
currentStore = ""
currentOrderID = ""
AddID = 90

"""Temporary usernames, add SQL queries later"""
"""
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
"""

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
			db.create_table()
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


@app.route('/registrationType', methods=['GET','POST'])
def registrationType():
	return render_template('registrationType2.html')


@app.route('/registerBuyer', methods=['GET','POST'])
def registerBuyer():
	store = db.listStores()
	return render_template('registerBuyer3.html', store=store)

@app.route('/checkregisterBuyer', methods=['GET','POST'])
def checkregisterBuyer():

	if request.method == "POST":
		uname = request.form['uname']
		fname = request.form['fname']
		lname = request.form['lname']
		password = request.form['password']
		email = request.form['email']
		street = request.form['street']
		houseNo = request.form['houseNo']
		city = request.form['city']
		lname = request.form['lname']
		phone = request.form['phone']
		cpassword = request.form['cpassword']
		state = request.form['state']
		zipp = request.form['zip']
		payment = request.form['payment']
		routingNo = request.form['routingNo']
		accNo = request.form['accNo']
		dsID = request.form['dsID']

		error1 = "your password is messed up bro"
		error2 = "phone has incorrect number of digits"
		error3 = "zip code has incorrect number of digits"
		error4 = "email has improper format"
		error5 = "C'mon brug you messed up your account number"
		error6 = "Lmao try dat routing number again"
		error7 = "phone has correct number of digits, motherfucker"
		arr = re.split(r'[@.]', email)
		if password != cpassword:
			return render_template("registerBuyer3.html", error=error1)
		elif (len(str(phone))) == 10:
			return render_template("registerBuyer3.html", error=error7)
		elif (len(str(phone))) != 9:#10:
			return render_template("registerBuyer3.html", error=error2)
		elif (len(str(zipp))) != 5:
			return render_template("registerBuyer3.html", error=error3)
		elif (len(arr) != 3) or (arr[0].isalnum() and arr[1].isalnum() and arr[2].isalnum())/1 != 1:
			return render_template("registerBuyer3.html", error=error4)
		elif (len(str(routingNo))) != 9:#10:
			return render_template("registerBuyer3.html", error=error5)
		elif (len(str(accNo))) != 9:#10:
			return render_template("registerBuyer3.html", error=error6)
		else:
			'''query = "SELECT MAX(id) FROM Address;"
			response = db.cursor.execute(query)
			db.cursor.fetchall()'''
			global AddID
			AddID = AddID + 1
			user_type = 'buyer'
			reg = db.insertUser(uname,password,user_type,email,fname,lname)
			if reg == 1:
				return render_template("registerBuyer3.html", error="Username is Taken.")
			reg = db.insertPayment(uname,payment,accNo,routingNo)
			if reg == 1:
				return render_template("registerBuyer3.html", error="Payment name already Used.")
			else:
				query = "INSERT INTO Payments(username,payment_name,account_number,routing_number)"\
				"VALUES (%s,%s,%s,%s);"
				db.cursor.execute(query, (uname,payment,accNo,routingNo))
				db.conn.commit()
			reg = db.insertAddress(AddID,houseNo,street,state,city,zipp)
			reg = db.insertBuyer(uname,phone,AddID,payment,dsID)
			return render_template('login1.html')

	return render_template('registerBuyer3.html', error="something wrong")


@app.route('/registerDeliverer', methods=['GET','POST'])
def registerDeliverer():
	return render_template('registerDeliverer4.html')

@app.route('/checkregisterDeliverer', methods=['GET','POST'])
def checkregisterDeliverer():

	if request.method == "POST":
		fname = request.form['fname']
		uname = request.form['uname']
		password = request.form['password']
		email = request.form['email']
		lname = request.form['lname']
		cpassword = request.form['cpassword']
		confcode = request.form['code']

		error1 = "your password is messed up bro"
		error2 = "email contains non-alphanumeric characters"
		arr = re.split(r'[@.]', email)
		if password != cpassword:
			return render_template("registerDeliverer4.html", error=error1)
		elif (len(arr) != 3) or (arr[0].isalnum() and arr[1].isalnum() and arr[2].isalnum())/1 != 1:
			return render_template("registerDeliverer4.html", error=error2)
		else:
			user_type = 'deliverer'
			sysid = 0 #deliverer tag is 0 in system information
			reg = db.systeminfoDeliverer(sysid,confcode)
			if reg == 1:
				return render_template("registerDeliverer4.html", error="Code incorrect.")
			reg = db.insertUser(uname,password,user_type,email,fname,lname)
			if reg == 1:
				return render_template("registerDeliverer4.html", error="Username is Taken.")
			return render_template('login1.html')

	return render_template('registerDeliverer4.html', error="something wrong")



@app.route('/registerManager', methods=['GET','POST'])
def registerManager():
	store = db.listStores()
	return render_template('registerManager5.html', store=store)

@app.route('/checkregisterManager', methods=['GET','POST'])
def checkregisterManager():

	if request.method == "POST":
		fname = request.form['fname']
		uname = request.form['uname']
		password = request.form['password']
		email = request.form['email']
		lname = request.form['lname']
		cpassword = request.form['cpassword']
		confcode = request.form['code']
		dsID = request.form['dsID']

		error1 = "your password is messed up bro"
		error2 = "email contains non-alphanumeric characters"
		arr = re.split(r'[@.]', email)
		if password != cpassword:
			return render_template("registerManager5.html", error=error1)
		elif (len(arr) != 3) or (arr[0].isalnum() and arr[1].isalnum() and arr[2].isalnum())/1 != 1:
			return render_template("registerManager5.html", error=error2)
		else:
			user_type = 'manager'
			sysid = 1 #manager tag is 1 in system information
			reg = db.systeminfoManager(sysid,confcode)
			if reg == 1:
				return render_template("registerManager5.html", error="Code incorrect.")
			reg = db.insertUser(uname,password,user_type,email,fname,lname)
			if reg == 1:
				return render_template("registerManager5.html", error="Username is Taken.")
			reg = db.insertManager(uname,dsID)
			return render_template('login1.html')
	return render_template('registerManager5.html', error="something wrong")

@app.route('/listOfStores', methods=['GET','POST'])
def listOfStores():
	info = db.listStores()

	return render_template('listOfStores8.html' , info=info)

@app.route('/checkStoreHomepage', methods=['GET','POST'])
def checkSToreHomepage():
	global currentStore
	db.create_table()
	if request.method == "POST":
		currentStore = request.form["store"]
		print(currentStore)
		return render_template('storeHomepage9.html')

@app.route('/storeHomepage', methods=['GET','POST'])
def storeHomepage():
	return render_template('storeHomepage9.html')

"""
@app.route('/buyerAccountInfo', methods=['GET','POST'])
def buyerAccountInfo():
	return buyerAccInfo()
"""

@app.route('/buyerAccountInfo', methods=['GET','POST'])
def buyerAccountInfo():
	#currentUser = 'admirableneville'
	dictry =  db.selectBuyerInfo(currentUser)
	store = db.listStores()
	"""
	store = []
	for i in range(1,36):
		if i == int(dictry['defaultStore']):
			store.append(" selected ")
		else:
			store.append(" ")
	"""

	return render_template("buyerAccountInfo7.html", dictry=dictry, store=store)

@app.route('/updateBuyerAccountInfo', methods=['GET','POST'])
def updateBuyerAccountInfo():
	if request.method == "POST":
		fname = request.form['fname']
		lname = request.form['lname']
		prefStore = request.form['prefStore']
		email = request.form['email']
		prefCard = request.form['prefCard']
		routingNo = request.form['routingNo']
		phone = request.form['phone']
		houseNo = request.form['houseNo']
		streetAddress = request.form['streetAddress']
		city = request.form['city']
		state = request.form['state']
		zipp = request.form['zip']

		arr = re.split(r'[@.]', email)
		error1 = "phone has incorrect number of digits"
		error2 = "zip code has incorrect number of digits"
		error3 = "email contains non-alphanumeric characters"
		dictry = db.selectBuyerInfo(currentUser)
		store = db.listStores()
		if (len(str(phone))) != 9:#10:
			return render_template("buyerAccountInfo7.html", error=error1, dictry=dictry, store=store)
		elif (len(str(zipp))) != 5:
			return render_template("buyerAccountInfo7.html", error=error2, dictry=dictry, store=store)
		elif (len(arr) != 3) or (arr[0].isalnum() and arr[1].isalnum() and arr[2].isalnum())/1 != 1:
			return render_template("buyerAccountInfo7.html", error=error3, dictry=dictry, store=store)
		else:
			val = db.updateBuyerInfo(currentUser,prefStore,email,prefCard,routingNo,phone,houseNo,streetAddress,city,state,zipp,fname,lname)
			dictry = db.selectBuyerInfo(currentUser)
			store = db.listStores()
			if val == 0:
				return render_template("buyerAccountInfo7.html", error = "Updates Saved", dictry=dictry, store=store)
			else:
				return render_template("buyerAccountInfo7.html",error = "SQL query error", dictry=dictry, store=store)
	return render_template("buyerFunctionality6.html", error = "ah shit here we go again")

@app.route('/deleteAccountInfo', methods=['GET','POST'])
def deleteAccountInfo():
	uname = currentUser
	query = "DELETE FROM Userr WHERE username = %s"
	db.cursor.execute(query, uname)
	db.conn.commit()
	return render_template('login1.html', error = "See ya, wouldn't wanna be ya!")

@app.route('/findItem', methods=['GET','POST'])
def findItem():
	return render_template('findItem10.html')


"""
@app.route('/itemType', methods=['GET','POST'])
def litemType():
	if request.method == 'POST':

		Itype = request.form['name']
		itemTypeI(Itype)

		@app.route('/itemType/<Itype>', methods=['GET','POST'])
		def itemTypeI(Itype):
			return render_template('itemType11.html', Itype=Itype)



"""
@app.route('/itemType', methods=['GET','POST'])
def itemTypeI():
	if request.method=='POST':
		Itype = request.form['Itype']
	info = db.popItem(Itype, currentStore)
	return render_template('itemType11.html', Itype=Itype, info=info)



@app.route('/cart', methods=['GET','POST'])
def cart():
	info = db.popCart()
	return render_template('cart12.html', info=info)

@app.route('/addToCart', methods=['GET','POST'])
def addToCart():
	quantity = request.form['quantity']
	itemID = request.form['itemID']
	val = db.addToCart(quantity,itemID)
	info = db.popCart()
	if val == 1:
		#return itemTypeI(itemName, error)
		return render_template('itemType11.html', error = "Item already exists, try editing the item in the cart page.", info=info)
	else:
		#return itemTypeI(itemName, error)
		return render_template('itemType11.html', error = "Item Added. Please Select View Cart to View the Items Currently in Your Cart.", info=info)

@app.route('/deleteFromCart', methods=['GET','POST'])
def deleteFromCart():
	itemID = request.form['itemID']
	val = db.deleteFromCart(itemID)
	info = db.popCart()
	return render_template('cart12.html', error = "Item Deleted", info=info)

@app.route('/adjustCart', methods=['GET','POST'])
def adjustCart():
	quantity = request.form['quantity']
	itemID = request.form['itemID']
	val = db.adjustCart(quantity,itemID)
	info = db.popCart()
	return render_template('cart12.html', error = "Item quantity adjusted.", info=info)

@app.route('/checkout', methods=['GET','POST'])
def checkout():
	#query = "SELECT sum( CartView.quantity*Item.listed_price) Item join CartView on Item.item_id=CartView.Item_id"
	#db.cursor.execute(query)
	#total = db.cursor.fetchone()
	#db.cursor.fetchall()
	total = db.orderTot()
	return render_template('checkout13.html',total=total)


@app.route('/paymentMethods', methods=['GET','POST'])
def paymentMethods():
	payment = db.paymentMeth(currentUser)
	return render_template('paymentMethods14.html', payment= payment )

@app.route('/newPayment', methods=['GET','POST'])
def newPayment():
	return render_template('newPayment15.html')

@app.route('/addNewPayment', methods=['GET','POST'])
def addNewPayment():
	if request.method == "POST":
		payment = request.form['payment']
		accName = request.form['accName']
		routingNo = request.form['routingNo']

		val = db.addNewPay(currentUser,payment,accName,routingNo)
		if val == 0:
			payment = db.paymentMeth(currentUser)
			return render_template('paymentMethods14.html',error = "Payment Added", payment= payment )
		else:
			return render_template("newPayment15.html",error = "Payment Type Already Used")
	return render_template("newPayment15.html", error = "Sum Ting Wong")

@app.route('/changeDefaultPayment', methods=['GET','POST'])
def changeDefaultPayment():
	if request.method == "POST":
		paymentName = request.form['paymentName']
		val = db.updateDefaultPayment(currentUser,paymentName)
		payment = db.paymentMeth(currentUser)
		return render_template('paymentMethods14.html',error = "Default Payment Updated", payment= payment )

	return render_template("newPayment15.html", error = "Wii Tu Lo")


@app.route('/reciept', methods=['GET','POST'])
def reciept():
	"""
	if request.method == "POST":
		payment = request.form['payment']
		deliveryTime = request.form['deliveryTime']
		deliveryInstruc = request.form['deliveryInstruc']
	"""
	dictry, noItems, payment = db.reciept(currentOrderID, currentUser)
	return render_template('reciept16.html', dictry = dictry, noItems=noItems, payment=payment)

@app.route('/orderHistory', methods=['GET','POST'])
def orderHistory():
	info = db.orderHist(currentUser)
	isDel = []

	count = 0
	"""
	for i in info:

		if int(i[5]) == 1:
			info[count,5] = 'Yes'
		else:
			info[count,5] = 'No'
		count = count +1
	"""
	"""
	print (  info )
	#temp = ()
	for i in info:
		if int( i[5]) == 1:
			a = ('Yes'),

		else:
			a = ('No'),
			temp = (temp + a),

	#info.append(isDel)
	print (  temp )
	"""
	return render_template('orderHistory17.html', info=info, isDel=isDel)





@app.route('/delivererFunctionality', methods=['GET','POST'])
def delivererFunctionality():
	return render_template('delivererFunctionality18.html')

@app.route('/delivererAccInfo', methods=['GET','POST'])
def delivererAccInfo():
	dictry = db.selectDelivererInfo(currentUser)
	return render_template('delivererAccountInfo19.html', dictry=dictry)

@app.route('/updateDelivererAccInfo', methods=['GET','POST'])
def updateDelivererAccInfo():
	if request.method == "POST":
		fname = request.form['fname']
		lname = request.form['lname']
		email = request.form['email']

		arr = re.split(r'[@.]', email)
		error1 = "email contains non-alphanumeric characters"
		dictry = db.selectDelivererInfo(currentUser)
		if (len(arr) != 3) or (arr[0].isalnum() and arr[1].isalnum() and arr[2].isalnum())/1 != 1:
			return render_template("delivererAccountInfo19.html", error=error1, dictry=dictry)
		else:
			val = db.updateDelivererInfo(currentUser, email, fname, lname)
			dictry = db.selectDelivererInfo(currentUser)
			if val == 0:
				return render_template("delivererAccountInfo19.html", error = "Updates Saved", dictry=dictry)
			else:
				return render_template("delivererAccountInfo19.html",error = "SQL query error", dictry=dictry)
	return render_template("delivererAccountInfo19.html", error = "Something Wrong")

@app.route('/assignments', methods=['GET','POST'])
def assignments():
	info = db.assignments(currentUser)
	return render_template('assignments20.html', info=info)

@app.route('/assignment', methods=['GET','POST'])
def assignment():
	if request.method == "POST":
		global currentOrderID
		currentOrderID = request.form["store"]
		dictry, iandq = db.newAss(currentUser,currentOrderID)
		return render_template('assignment21.html',dictry = dictry, iandq=iandq)
	return render_template('assignment21.html', error = "lmao something is really messed up.")




@app.route('/managerFunctionality', methods=['GET','POST'])
def managerFunctionality():
	return render_template('managerFunctionality22.html')

@app.route('/managerAccInfo', methods=['GET','POST'])
def managerAccInfo():
	dictry = db.selectManagerInfo(currentUser)
	stores = db.listStores()
	sel = ()
	"""
	print (stores)
	count = int(0)
	for i in range(1,len(stores[0])+1):
		if i == int(dictry['storeID']):
			sel = sel + ( stores[0,count], stores[1,count] , "selected"),
		else:
			sel = sel +  ( stores[0,count], stores[1,count] , " "),
		count = count + 1
	print(sel)
	"""
	return render_template('managerAccountInfo23.html', dictry=dictry, stores=stores, sel=sel)

@app.route('/updateManagerAccInfo', methods=['GET','POST'])
def updateManagerAccInfo():
	if request.method == "POST":
		fname = request.form['fname']
		lname = request.form['lname']
		email = request.form['email']

		arr = re.split(r'[@.]', email)
		'''error1 = "phone has incorrect number of digits"
		error2 = "zip code has incorrect number of digits"'''
		error1 = "email contains non-alphanumeric characters"
		dictry = db.selectManagerInfo(currentUser)
		stores = db.listStores()
		sel = ()
		'''if (len(str(phone))) != 9:#10:
			return render_template("managerAccountInfo23.html", error=error1, dictry=dictry, stores=stores, sel=sel)
		elif (len(str(zipp))) != 5:
			return render_template("managerAccountInfo23.html", error=error2, dictry=dictry, stores=stores, sel=sel)'''
		if (len(arr) != 3) or (arr[0].isalnum() and arr[1].isalnum() and arr[2].isalnum())/1 != 1:
			return render_template("managerAccountInfo23.html", error=error1, dictry=dictry, stores=stores, sel=sel)
		else:
			val = db.updateManagerInfo(currentUser,email,fname,lname)
			dictry = db.selectManagerInfo(currentUser)
			stores = db.listStores()
			sel = ()
			if val == 0:
				return render_template("managerAccountInfo23.html", error = "Updates Saved", dictry=dictry, stores=stores, sel=sel)
			else:
				return render_template("managerAccountInfo23.html",error = "SQL query error", dictry=dictry, stores=stores, sel=sel)
	return render_template("managerAccountInfo23.html", error = "Something Wrong")

@app.route('/revenueReport', methods=['GET','POST'])
def revenueReport():
	dictry = db.revenueRep(currentUser)
	return render_template('revenueReport24.html', dictry=dictry)

@app.route('/outstandingOrders', methods=['GET','POST'])
def outstnadingOrders():
	info = db.outstandingOrders(currentUser)
	return render_template('outstandingOrders25.html', info=info)



@app.route('/inventory', methods=['GET','POST'])
def inventory():
	info = db.inventory(currentUser)
	count = 0
	for i in info:
		count = count + i[2]

	return render_template('inventory26.html', info=info, count = count)

@app.route('/viewOrderDetails', methods=['GET','POST'])
def viewOrderDetails():
	return render_template('inventory26.html')


@app.route('/updateDeliveryInfo', methods=['GET','POST'])
def updateDeliveryInfo():

	if request.method == "POST":
		status = request.form['status']
		if int(status) == 0:
			print("fuck")
			info = db.assignments(currentUser)
			return render_template('assignments20.html', info=info)
		else:
			print("yeeET")
			db.updateDelivery(currentUser, currentOrderID)
			print(currentOrderID)
			print(currentUser)
			info = db.assignments(currentUser)
			return render_template('assignments20.html', info=info)
	info = db.assignments(currentUser)
	return render_template('assignments20.html', info=info)

@app.route('/viewItemM', methods=['GET','POST'])
def viewItem():
	if request.method == "POST":
		itemNo = request.form['itemNo']
		dictry = db.getItemInfo(itemNo)
		return render_template("viewItemM.html",  dictry=dictry)

	return


@app.route('/viewOrderB', methods=['GET','POST'])
def viewOrderB():
	if request.method == "POST":
		orderID = request.form['store']
		dictry = db.getOrderInfo(currentUser, orderID)
		return render_template("viewOrderB.html",  dictry=dictry, orderID=orderID)

	return orderHistory()

@app.route('/checkCheckout', methods=['GET','POST'])
def checkCheckout():
	if request.method == "POST":
		payment = request.form['payment']
		deliveryInstructions = request.form['deliveryInstructions']
		deliveryTime = request.form['deliveryTime']
		dictry = db.selectBuyerInfo(currentUser)
		global currentOrderID
		print(payment + "first")
		if payment == "Other":
			return paymentMethods()
		else:
			global currentStore
			newOrderID = 1000000
			query = db.getNewOrderID()
			for i in query:
				if i[0] == newOrderID:
					newOrderID = newOrderID + 1
			currentOrderID = newOrderID
			db.updateOrder(currentUser,currentStore,currentOrderID,deliveryInstructions, deliveryTime)
			return reciept()
	return


if __name__ == '__main__' :
	app.run()
