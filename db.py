import pymysql

conn = pymysql.connect(host="localhost",
							db="GroceryTech",
							user="root",
							passwd='CornyJoke12')
cursor = conn.cursor()


def tuplesToList(tlist):
    newlist = []
    for i in tlist:
        newlist.append(i)
    return newlist


# returns 0 if credentials are invalid
# returns 1 if user is a manager
# returns 2 if user is NOT a manager
def login(username, password):
    query = "SELECT COUNT(*) FROM userr WHERE username = %s AND password = %s;"
    response = cursor.execute(query, (username, password))
    for i in cursor:
        i = (i[0])
    # clear cursor
    cursor.fetchall()
    if i == 0:
        return 0
    else:
        query = "SELECT user_type FROM userr WHERE username = %s;"
        response = cursor.execute(query, (username))

        result = cursor.fetchone()
        print(result[0])
        # sanity check
        cursor.fetchall()
        print(result[0])
        if result[0] == 'manager':  # if Is_manager
            return 1
        elif result[0] == 'deliverer':
            return 2
        else:
            return 3

def insertUser(uname,password,user_type,email,fname,lname):
    query = "SELECT COUNT(username) FROM Userr WHERE username=%s"
    cursor.execute(query, uname)
    for i in cursor:
        response = i[0]
    #return cursor
    cursor.fetchall()
    if response != 1:
        query = "INSERT INTO Userr(username,password,user_type,email,first_name,last_name)"\
        "VALUES (%s,%s,%s,%s,%s,%s);"
        cursor.execute(query, (uname,password,user_type,email,fname,lname))
        conn.commit()
        return 0
    else:
        return 1
        #return 0

def insertManager(uname,dsID):
    query = "SELECT address_id FROM GroceryStore WHERE store_id = %s"
    cursor.execute(query, dsID)
    for i in cursor:
        response = i[0]
        print(response)
    #return cursor
    cursor.fetchall()
    query = "INSERT INTO manages(username,store_address)"\
    "VALUES (%s,%s);"
    cursor.execute(query, (uname,response))
    conn.commit()

def insertBuyer(Username, Phone, AddressID, DefaultPayment, DefaultStoreID):
    query = "INSERT INTO Buyer(username, phone, address_id, default_payment, default_store_id)"\
    "VALUES (%s,%s,%s,%s,%s);"
    cursor.execute(query, (Username, Phone, AddressID, DefaultPayment, DefaultStoreID))

    conn.commit()


def insertAddress(AddID,house_num,street,state,city,zipp):
    query = "INSERT INTO Address(id,house_number,street,state,city,zip_code)"\
    "VALUES (%s,%s,%s,%s,%s,%s);"
    '''AddID = int(AddID)
    house_num = int(house_num)
    zipp = int(zipp)'''
    cursor.execute(query, (AddID,house_num,street,state,city,zipp))
    # clear cursor
    conn.commit()

def systeminfoDeliverer(sysID,code):
    query = "SELECT user_codes FROM SystemInformation WHERE system_id = 0"
    cursor.execute(query)
    for i in cursor:
        res = i[0]
    cursor.fetchall()
    code = int(code)
    if res == code:
        return 0
    else:
        return 1

def systeminfoManager(sysID, code):
	query = "SELECT user_codes FROM SystemInformation WHERE system_id = 1"
	cursor.execute(query)
	for i in cursor:
		res = i[0]
	cursor.fetchall()
	code = int(code)
	if res == code:
		return 0
	else:
		return 1

def insertPayment(uname,payment,accNo,routingNo):
    query = "SELECT COUNT(*) FROM Payments WHERE username = %s AND payment_name = %s"
    cursor.execute(query, (uname,payment))
    for i in cursor:
        res = i[0]
    cursor.fetchall()
    if res == 0:
        return 0
    else:
        return 1


def selectBuyerInfo(uname):

	cursor.execute("SELECT * FROM Buyer Where username=%s",uname)
	username, phone, address, default_payment, default_store = cursor.fetchone()
	dictry = {}
	dictry['uname'] = username
	dictry['phone'] = phone
	dictry['address'] = address
	dictry['defaultPay'] = default_payment
	dictry['defaultStore'] = default_store
	cursor.execute("SELECT * FROM Userr Where username=%s",uname)
	username, password, userType, email, first_name, last_name = cursor.fetchone()
	dictry['email'] = email
	dictry['fname'] = first_name
	dictry['lname'] = last_name
	cursor.execute("SELECT * FROM Address Where id=%s",address)
	addid, house, street, city, state, zipp = cursor.fetchone()
	dictry['houseNo'] = house
	dictry['street'] = street
	dictry['city'] = city
	dictry['state'] = state
	dictry['zipp'] = zipp
	cursor.execute("SELECT * FROM Payments Where username=%s",uname)
	uname, payment, account, routing = cursor.fetchone()
	dictry['payment'] = payment
	dictry['account'] = account
	dictry['routing'] = routing
	cursor.execute("SELECT * FROM GroceryStore Where store_id=%s",default_store)
	store_id, storeName,address_id,b,c,d = cursor.fetchone()
	dictry['storeName'] = storeName


	return dictry

def updateBuyerInfo(uname,prefStore,email,prefCard,routingNo,phone,houseNo,streetAddress,city,state,zipp,fname,lname):
    query = "UPDATE Userr SET first_name = %s, last_name = %s, email = %s WHERE Username = %s;"
    cursor.execute(query, (fname,lname,email,uname))
    # clear cursor
    conn.commit()
    query = "SELECT default_store_id FROM Buyer WHERE username = %s"
    cursor.execute(query, (uname))
    storeID = cursor.fetchone()
    cursor.fetchall()
    query = "UPDATE Buyer SET phone = %s, default_store_id = %s WHERE Username = %s;"
    cursor.execute(query, (phone,prefStore,uname))
    # clear cursor
    conn.commit()
    query = "SELECT address_id FROM Buyer WHERE username = %s"
    cursor.execute(query, (uname))
    addID = cursor.fetchone()
    cursor.fetchall()
    query = "UPDATE Address SET house_number = %s, street = %s, city = %s, state = %s, zip_code = %s WHERE id = %s;"
    cursor.execute(query, (houseNo,streetAddress,city,state,zipp,addID))
    # clear cursor
    conn.commit()


    query = "SELECT default_payment FROM Buyer WHERE username = %s"
    cursor.execute(query, (uname))
    payname = cursor.fetchone()
    cursor.fetchall()
    query = "UPDATE Payments SET account_number = %s, routing_number = %s WHERE Username = %s AND payment_name = %s;"
    cursor.execute(query, (prefCard,routingNo,uname,payname))
    # clear cursor
    conn.commit()

    return 0

def selectDelivererInfo(uname):
	cursor.execute("SELECT * FROM Userr Where username=%s",uname)
	username, password, userType, email, first_name, last_name = cursor.fetchone()
	dictry = {}
	dictry['uname'] = username
	dictry['email'] = email
	dictry['fname'] = first_name
	dictry['lname'] = last_name
	return dictry

def updateDelivererInfo(uname,email):
    query = "UPDATE Userr SET email = %s WHERE Username = %s;"
    cursor.execute(query, (email,uname))
    # clear cursor
    conn.commit()

    return 0



def selectManagerInfo(uname):
	cursor.execute("SELECT * FROM Userr Where username=%s",uname)
	username, password, userType, email, first_name, last_name = cursor.fetchone()
	dictry = {}
	dictry['uname'] = username
	dictry['email'] = email
	dictry['fname'] = first_name
	dictry['lname'] = last_name
	cursor.execute("SELECT * FROM manages Where username=%s",uname)
	username , store_id = cursor.fetchone()
	cursor.execute("SELECT * FROM GroceryStore Where address_id=%s",store_id)
	store_id, storename, address_id, opening, closing, phone = cursor.fetchone()
	dictry['storename'] = storename
	dictry['storeID'] = store_id
	dictry['phone'] = phone
	cursor.execute("SELECT * FROM Address Where id=%s",address_id)
	addid, house, street, city, state, zipp = cursor.fetchone()
	dictry['houseNo'] = house
	dictry['street'] = street
	dictry['city'] = city
	dictry['state'] = state
	dictry['zipp'] = zipp
	return dictry

def updateManagerInfo(uname, prefStore,email,phone,houseNo,streetAddress,city,state,zipp):
    query = "UPDATE Userr SET email = %s WHERE Username = %s;"
    cursor.execute(query, (email,uname))
    # clear cursor
    conn.commit()
    #following query was for checking to see if the addess inputted in is correct, though we figured that the manager should not be able to just change the address of the store.
    '''query = "SELECT id FROM Address WHERE houseNo = %s AND street = %s AND city = %s AND state = %s AND zip_code = %s"
    cursor.execute(query, (houseNo,streetAddress,city,state,zipp))
    storeID = cursor.fetchone()
    cursor.fetchall()
    if sum(storeID) == 0:
        return 1'''
    # query = "SELECT store_address FROM manages WHERE username = %s"
    # cursor.execute(query, (uname))
    # storeID = cursor.fetchone()
    # cursor.fetchall()
    query = "UPDATE manages SET store_address = %s WHERE username = %s;"
    cursor.execute(query, (prefStore,uname))
    # clear cursor
    conn.commit()
    query = "UPDATE GroceryStore SET phone = %s WHERE store_id = %s;"
    cursor.execute(query, (phone,prefStore))
    # clear cursor
    conn.commit()

    return 0

def reciept(orderID):
	dictry = {}
	cursor.execute("SELECT * FROM Order Where order_id=%s",orderID)
	oid, instructions, delivTime, orderPlacedDate, orderPlacedTime = cursor.fetchone()
	cursor.execute("SELECT * FROM DeliveredBy Where order_id=%s",orderID)
	oid, dusername, isDel, delTime, delDate = cursor.fetchone()
	cursor.execute("SELECT first_name, last_name FROM DeliveredBy Where order_id=%s",orderID)
	dictry['orderID'] = oid
	dictry['payment'] = ""
	dictry['fname'] = fname
	dictry['lname'] = lname
	dictry['noItems'] = noItems
	dictry['deliveryTime'] = delTime
	dictry['orderTime'] = orderPlacedTime

	return dictry

def revenueRep(uname):
	#SELECT DATEADD(yy, DATEDIFF(yy, 0, GETDATE()) - 1, 0))
	dictry = {}
	cursor.execute("SELECT * FROM manages Where username=%s",uname)
	username , store_id = cursor.fetchone()
	cursor.execute("SELECT * FROM GroceryStore Where address_id=%s",store_id)
	store_id, storename, address_id, opening, closing, phone = cursor.fetchone()
	dictry['storename'] = storename
	"""
	item_id = cursor.execute("SELECT item_id FROM soldAt JOIN manages ON soldAt.store_id=manages.store_address AND manages.username= %s",uname)
	dictry['itemCount'] = item_id

	"""
	cursor.execute("SELECT SUM(selectItem.quantity), SUM(Item.listed_price*selectItem.quantity-Item.wholesale_price*selectItem.quantity) FROM Item JOIN selectItem ON Item.item_id=selectItem.item_id WHERE selectItem.order_id IN (SELECT orderFrom.order_id FROM orderFrom WHERE orderFrom.store_address_id IN (SELECT GroceryStore.store_id FROM GroceryStore WHERE GroceryStore.address_id IN (SELECT manages.store_address FROM manages WHERE manages.username=%s)))", uname)
	#cursor.execute("SELECT COUNT(Item.listed_price*selectItem.quantity), SUM(Item.listed_price*selectItem.quantity-Item.wholesale_price*selectItem.quantity) FROM Item JOIN selectItem ON Item.item_id=selectItem.item_id WHERE selectItem.order_id IN (SELECT order_id FROM Orderr) AND selectItem.item_id IN (SELECT item_id FROM soldAt JOIN manages ON soldAt.store_id=manages.store_address AND manages.username= %s)",uname)
	#itemCount, revenue =  cursor.execute("SELECT COUNT(Item.listed_price*selectItem.quantity),SUM(Item.listed_price*selectItem.quantity-Item.wholesale_price*selectItem.quantity) FROM Item JOIN selectItem on Item.item_id=selectItem.item_id Where selectItem.order_id in (select order_id from Order where Order.order_placed_date > 2018-07-23  AND selectItem.item_id in(SELECT item_id from SoldAt JOIN manages on SoldAt.store_address=manages.store_address and manages.username = username=%s",uname)
	itemCount, revenue =  cursor.fetchone()
	dictry['itemCount'] = itemCount
	dictry['revenue'] = revenue

	return dictry

def assignments(uname):
	#cursor.execute("SELECT * FROM Orderr")
	cursor.execute("SELECT GroceryStore.store_name, Orderr.order_id, Orderr.order_placed_date, Orderr.order_placed_time, Orderr.delivery_time, SUM(selectItem.quantity*Item.listed_price), COUNT(selectItem.quantity) FROM GroceryStore Join orderFrom on GroceryStore.store_id=orderFrom.store_address_id Join Orderr on Orderr.order_id=orderFrom.order_id Join selectItem on selectItem.order_id=Orderr.order_id Join Item on Item.item_id=selectItem.item_id join deliveredBy on deliveredBy.order_id=Orderr.order_id where deliveredBy.deliverer_username=%s group by Orderr.order_id", uname)
	info = tuplesToList(cursor.fetchall())
	#a, b, c, d, e = cursor.fetchone()
	#store, orderID, orderDate, orderTime, noItems, quantity = cursor.fetchone()
	return info

def assignment(uname,orderID):
    dictry = {}
    query = "SELECT Item.item_name,selectItem.quantity FROM selectItem JOIN Item ON Item.item_id=selectItem.item_id WHERE selectItem.order_id = %s IN (SELECT orderedBy.order_id FROM orderedBy WHERE orderedBy.buyer_username = %s )"
    cursor.execute(query, (orderID, uname))
    iandq = tuplesToList(cursor.fetchall())

    query = "SELECT order_placed_time FROM Orderr WHERE order_id = %s"
    cursor.execute(query, (orderID))
    order_placed =  cursor.fetchone()
    dictry['order_placed'] = order_placed
    cursor.fetchall()

    query = "SELECT delivery_time FROM Orderr WHERE order_id = %s"
    cursor.execute(query, (orderID))
    delivery_time =  cursor.fetchone()
    dictry['delivery_time'] = delivery_time
    cursor.fetchall()

    query = "SELECT deliveredBy.isDelivered FROM deliveredBy WHERE deliveredBy.order_id = %s"
    cursor.execute(query, (orderID))
    status =  cursor.fetchone()
    dictry['status'] = status
    cursor.fetchall()

    query = "SELECT orderFrom.store_address FROM orderFrom WHERE orderFrom.order_id = %s"
    cursor.execute(query, (orderID))
    storeID =  cursor.fetchone()
    cursor.fetchall()
    query = "SELECT store_name FROM GroceryStore WHERE store_id = %s"
    cursor.execute(query, (storeID))
    storeName =  cursor.fetchone()
    dictry['storeName'] = storeName
    cursor.fetchall()

    query = "SELECT Orderr.delivery_instructions FROM Orderr WHERE order_id = %s"
    cursor.execute(query, (orderID))
    delivery_instructions =  cursor.fetchone()
    dictry['delivery_instructions'] = delivery_instructions
    cursor.fetchall()

    query = "SELECT orderedBy.buyer_username FROM orderedBy WHERE order_id = %s"
    cursor.execute(query, (order_id))
    buser =  cursor.fetchone()
    cursor.fetchall()
    query = "SELECT address_id FROM Buyer WHERE username = %s"
    cursor.execute(query, (uname))
    aID =  cursor.fetchone()
    cursor.fetchall()
    query = "SELECT house_number, street, city, state, zipcode FROM Addresses WHERE address_id = %s"
    cursor.execute(query, (aID))
    houseNo, street, city, state, zipp = cursor.fetchone()
    
	
    dictry['houseNo'] = houseNo
    dictry['street'] = street
    dictry['city'] = city
    dictry['state'] = state
    dictry['zipp'] = zipp

    return dictry, iandq

def orderHist(uname):
	cursor.execute("SELECT GroceryStore.store_name, Orderr.order_id, Orderr.order_placed_date, SUM(selectItem.quantity*Item.listed_price), COUNT(selectItem.quantity), DeliveredBy.is_delivered FROM GroceryStore Join orderFrom on GroceryStore.store_id=orderFrom.store_address_id Join Orderr on Orderr.order_id=orderFrom.order_id Join selectItem on selectItem.order_id=Orderr.order_id Join Item on Item.item_id=selectItem.item_id join deliveredBy on deliveredBy.order_id=Orderr.order_id join orderedBy on orderedBy.order_id=Orderr.order_id where orderedBy.buyer_username=%s group by Orderr.order_id",uname)
	#cursor.execute("SELECT GroceryStore.store_name, Orderr.order_id, Orderr.order_placed_date, SUM(selectItem.quantity*Item.listed_price), COUNT(selectItem.quantity), DeliveredBy.is_delivered FROM GroceryStore Join orderFrom on GroceryStore.store_id=orderFrom.store_address_id Join Orderr on Orderr.order_id=orderFrom.order_id Join selectItem on selectItem.order_id=Orderr.order_id Join Item on Item.item_id=selectItem.item_id join deliveredBy on deliveredBy.order_id=Orderr.order_id where orderedBy.buyer_username=%s group by Orderr.order_id", uname)
	info = tuplesToList(cursor.fetchall())
	#info.append("")
	return info

def listStores():
	cursor.execute("SELECT GroceryStore.store_id, GroceryStore.store_name, Address.house_number, Address.street, Address.city, Address.state, Address.zip_code, GroceryStore.phone, GroceryStore.opening_time, GroceryStore.closing_time FROM GroceryStore JOIN Address ON Address.id=GroceryStore.address_id")
	"""
	storeID, storeName, house, street, city, state, zipp, phone, opening, closing = cursor.fetchone()
	dictry = {}
	dictry["storeID"] = storeID
	dictry["storeName"] = storeName
	dictry["house"] = house
	dictry["street"] = street
	dictry["city"] = city
	dictry["state"] = state
	dictry["zip"] = zipp
	dictry["phone"] = phone
	dictry["open"] = opening
	dictry["close"] = closing
	"""
	info = tuplesToList(cursor.fetchall())
	return info



def paymentMeth(uname):
	cursor.execute("SELECT Buyer.default_payment, Payments.payment_name, Payments.account_number, Payments.routing_number FROM Buyer join Payments ON Payments.username = Buyer.username WHERE Buyer.username=%s", uname)
	info = tuplesToList(cursor.fetchall())
	return info

def addNewPay(uname,payment,accName,routingNo):
    #first check if payment method already exists
    query = "SELECT Count(*) FROM Payments WHERE username = %s AND payment_name = %s"
    cursor.execute(query, (uname,payment))
    payexist = cursor.fetchone()
    print(payexist)
    cursor.fetchall()
    if payexist != (0,):
        return 1
    query = "INSERT INTO Payments(username, payment_name, account_number, routing_number)"\
    "VALUES (%s,%s,%s,%s);"
    cursor.execute(query, (uname,payment,accName,routingNo))

    conn.commit()
    return 0

def updateDefaultPayment(uname,payment):
    query = "UPDATE Buyer SET default_payment = %s WHERE Username = %s;"
    cursor.execute(query, (payment,uname))
    # clear cursor
    conn.commit()
    return



def popItem(itemName, storeID):
	cursor.execute("SELECT Item.quantity, Item.item_name, Item.description, Item.exp_date, Item.listed_price, Item.item_id FROM Item join soldAt on soldAt.item_id=Item.item_id where Item.food_group=%s and soldAt.store_id=%s",(itemName,storeID))
	#cursor.execute("SELECT Item.quantity, Item.item_name, Item.description, Item.exp_date, Item.listed_price, Item.item_id FROM Item WHERE Item.food_group=%s",itemName)
	info  = tuplesToList(cursor.fetchall())
	return info


def inventory(uname):
	cursor.execute("SELECT Item.item_name, Item.description, Item.quantity, Item.listed_price, Item.wholesale_price, Item.exp_date From Item Join soldAt on Item.item_id=soldAt.item_id WHERE soldAt.store_id IN (SELECT GroceryStore.store_id FROM GroceryStore Where GroceryStore.address_id IN (SELECT manages.store_address From manages WHERE manages.username=%s)) ",uname)
	#cursor.execute("SELECT Item.item_name, Item.description, Item.quantity, Item.listed_price, Item.wholesale_price, Item.exp_date, From Item Join soldAt on soldAt.item_id = Item.item_id WHERE soldAt.store_id IN (SELECT GroceryStore.store_id FROM GroceryStore Where GroceryStore.address_id IN (SELECT manages.store_address From manages WHERE manages.username=%s) ",uname)
	info =  tuplesToList(cursor.fetchall())
	return info



def outstandingOrders(uname):
	cursor.execute("select GroceryStore.store_name, concat(A.house_number,', ',A.street,', ',A.city,', ',A.state,', ',A.state,', ',A.zip_code), orderFrom.order_id, Orderr.order_placed_date , selectItem.quantity*Item.listed_price, selectItem.quantity, concat(B.house_number,', ',B.street,', ',B.city,', ',B.state,', ',B.state,', ',B.zip_code) from orderFrom natural join Orderr natural join orderedBy natural join selectItem join deliveredby on orderFrom.order_id=deliveredBy.order_id join GroceryStore on GroceryStore.store_id=orderFrom.store_address_id join Buyer on Buyer.username=orderedBy.buyer_username join Address as A on A.id=GroceryStore.store_id join Item on Item.item_id=selectItem.item_id join Address as B on B.id=Buyer.address_id where GroceryStore.address_id in (select store_address from manages where username=%s) and deliveredBy.is_delivered=0",uname)
	info =  tuplesToList(cursor.fetchall())
	return info



