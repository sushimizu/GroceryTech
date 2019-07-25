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

def addToCart(quantity,itemID):
    print("asd")
    #check if item already exists in cart
    query = "SELECT quantity FROM CartView where Item_id = %s"
    cursor.execute(query,itemID)
    itemexist = cursor.fetchone()
    #print(itemexist)
    cursor.fetchall()
    print(itemexist)
    if itemexist != None:
        return 1
    else:
        query = "INSERT INTO CartView(quantity,Item_id)"\
        "VALUES (%s,%s);"
        cursor.execute(query, (quantity,itemID))
    # clear cursor
        conn.commit()
        return 0

def deleteFromCart(itemID):
    query = "DELETE FROM CartView where Item_id = %s"
    cursor.execute(query, itemID)
    cursor.fetchall()
    return

def adjustCart(quantity,itemID):
    query = "UPDATE CartView SET quantity = %s WHERE Item_id = %s;"
    cursor.execute(query, (itemID))
    # clear cursor
    conn.commit()
    return

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

def updateDelivererInfo(uname,email,fname,lname):
    query = "UPDATE Userr SET first_name = %s, last_name = %s, email = %s WHERE Username = %s;"
    cursor.execute(query, (fname,lname,email,uname))
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

def updateManagerInfo(uname,email,fname,lname):
    query = "UPDATE Userr SET first_name = %s, last_name = %s, email = %s WHERE Username = %s;"
    cursor.execute(query, (fname,lname,email,uname))
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
    '''query = "UPDATE manages SET store_address = %s WHERE username = %s;"
    cursor.execute(query, (prefStore,uname))
    # clear cursor
    conn.commit()
    query = "UPDATE GroceryStore SET phone = %s WHERE store_id = %s;"
    cursor.execute(query, (phone,prefStore))
    # clear cursor
    conn.commit()'''

    return 0



def updateOrder(uname,storeID,orderID,deliveryInstruc, deliveryTime):
    query = "INSERT INTO Orderr(order_id,delivery_instructions,delivery_time,order_placed_date,order_placed_time)"\
    "VALUES (%s,%s,%s,curdate(),curtime());"
    cursor.execute(query, (orderID,deliveryInstruc,deliveryTime))
    conn.commit()

    query = "INSERT INTO OrderedBy(order_id,buyer_username)"\
    "VALUES (%s,%s);"
    cursor.execute(query, (orderID,uname))
    conn.commit()

    query = "INSERT INTO orderFrom(store_address_id,order_id)"\
    "VALUES (%s,%s);"
    cursor.execute(query, (storeID,orderID))
    conn.commit()

    query = "SELECT * FROM CartView"
    cursor.execute(query)
    quantity, itemID = cursor.fetchone()
    cursor.fetchall()
    query = "INSERT INTO selectItem(item_id,quantity,order_id)"\
    "VALUES (%s,%s,%s);"
    cursor.execute(query, (itemID,quantity,orderID))
    conn.commit()
    cursor.execute("SELECT deliveredBy.deliverer_username FROM deliveredBy ORDER BY rand() limit 1 ")
    dusername = cursor.fetchone()
    #query = "INSERT INTO deliveredBy(order_id,deliverer_username,is_delivered,delivery_time,delivery_date)"\
    #"VALUES (%s,%s,%s,%s,%s);"

    #cursor.execute(query, (orderID,"SELECT deliverer_username from deliveredBy where is_delivered=0 group by deliverer_username order by count(deliverer_username) limit 1","0","",""))
    query = "INSERT INTO deliveredBy(order_id,deliverer_username,is_delivered,delivery_time,delivery_date)"\
    "VALUES (%s,%s,%s,%s,%s);"

    another_query="SELECT deliverer_username from deliveredBy where is_delivered=0 group by deliverer_username order by count(deliverer_username)"
    cursor.execute(another_query)
    name=cursor.fetchall()

    cursor.execute(query, (orderID,name[0][0],"0","",""))
    #cursor.execute(query, (orderID,"chivalrouspotatoes","0","",""))

    conn.commit()

    query = "UPDATE item set quantity=item.quantity - %s WHERE item_id = %s;"
    cursor.execute(query, (quantity,itemID))
    # clear cursor
    conn.commit()


def reciept(orderID, uname):
    dictry = {}
    cursor.execute("SELECT * FROM Orderr WHERE order_id=%s",orderID)
    oid, instructions, delivTime, orderPlacedDate, orderPlacedTime = cursor.fetchone()
    cursor.execute("SELECT * FROM DeliveredBy WHERE order_id=%s",orderID)
    oidd, dusername, isDel, delTime, delDate = cursor.fetchone()
    cursor.execute("SELECT Userr.first_name, Userr.last_name FROM Userr Join DeliveredBy ON Userr.username=DeliveredBy.deliverer_username WHERE deliveredBy.order_id=%s",oid)
    fname , lname = cursor.fetchone()
    cursor.execute("select sum(selectItem.quantity) from selectItem Where selectItem.order_id=%s", orderID)
    noItems = tuplesToList(cursor.fetchall())
    cursor.execute("select Buyer.default_payment from Buyer where Buyer.username=%s ",uname)
    payment = tuplesToList(cursor.fetchall())
    dictry['orderID'] = oid
    #dictry['payment'] = payment
    dictry['fname'] = fname
    dictry['lname'] = lname
    dictry['deliveryTime'] = delivTime
    dictry['orderTime'] = orderPlacedTime

    return dictry, noItems, payment

def revenueRep(uname):
	#SELECT DATEADD(yy, DATEDIFF(yy, 0, GETDATE()) - 1, 0))
	dictry = {}
	cursor.execute("SELECT * FROM manages Where username=%s",uname)
	username , store_id = cursor.fetchone()
	cursor.execute("SELECT * FROM GroceryStore Where address_id=%s",store_id)
	store_id, storename, address_id, opening, closing, phone = cursor.fetchone()
	dictry['storename'] = storename

	#item_id = cursor.execute("SELECT item_id FROM soldAt JOIN manages ON soldAt.store_id=manages.store_address AND manages.username= %s",uname)
	#dictry['itemCount'] = item_id





	cursor.execute("SELECT SUM(selectItem.quantity), SUM(Item.listed_price*selectItem.quantity-Item.wholesale_price*selectItem.quantity) FROM Item JOIN selectItem ON Item.item_id=selectItem.item_id join Orderr on selectItem.order_id=Orderr.order_id WHERE selectItem.order_id IN (SELECT orderFrom.order_id FROM orderFrom join Orderr on orderFrom.order_id=Orderr.order_id  WHERE orderFrom.store_address_id IN (SELECT GroceryStore.store_id FROM GroceryStore WHERE GroceryStore.address_id IN (SELECT manages.store_address FROM manages WHERE manages.username=%s)) and Orderr.order_placed_date > date_sub(curdate(),Interval 1 year))", uname)
    #cursor.execute("SELECT SUM(selectItem.quantity), SUM(Item.listed_price*selectItem.quantity-Item.wholesale_price*selectItem.quantity) FROM Item JOIN selectItem ON Item.item_id=selectItem.item_id WHERE selectItem.order_id IN (SELECT orderFrom.order_id FROM orderFrom WHERE orderFrom.store_address_id IN (SELECT GroceryStore.store_id FROM GroceryStore WHERE GroceryStore.address_id IN (SELECT manages.store_address FROM manages WHERE manages.username=%s)))", uname)
	#cursor.execute("SELECT COUNT(Item.listed_price*selectItem.quantity), SUM(Item.listed_price*selectItem.quantity-Item.wholesale_price*selectItem.quantity) FROM Item JOIN selectItem ON Item.item_id=selectItem.item_id WHERE selectItem.order_id IN (SELECT order_id FROM Orderr) AND selectItem.item_id IN (SELECT item_id FROM soldAt JOIN manages ON soldAt.store_id=manages.store_address AND manages.username= %s)",uname)
	#itemCount, revenue =  cursor.execute("SELECT COUNT(Item.listed_price*selectItem.quantity),SUM(Item.listed_price*selectItem.quantity-Item.wholesale_price*selectItem.quantity) FROM Item JOIN selectItem on Item.item_id=selectItem.item_id Where selectItem.order_id in (select order_id from Order where Order.order_placed_date > 2018-07-23  AND selectItem.item_id in(SELECT item_id from SoldAt JOIN manages on SoldAt.store_address=manages.store_address and manages.username = username=%s",uname)
	itemCount, revenue =  cursor.fetchone()
	dictry['itemCount'] = itemCount
	dictry['revenue'] = revenue

	return dictry

def assignments(uname):
	#cursor.execute("SELECT * FROM Orderr")
	cursor.execute("SELECT GroceryStore.store_name, Orderr.order_id, Orderr.order_placed_date, Orderr.order_placed_time, Orderr.delivery_time, SUM(selectItem.quantity*Item.listed_price), COUNT(selectItem.quantity) FROM GroceryStore Join orderFrom on GroceryStore.store_id=orderFrom.store_address_id Join Orderr on Orderr.order_id=orderFrom.order_id Join selectItem on selectItem.order_id=Orderr.order_id Join Item on Item.item_id=selectItem.item_id join deliveredBy on deliveredBy.order_id=Orderr.order_id where deliveredBy.deliverer_username=%s and deliveredBy.is_delivered=0 group by Orderr.order_id", uname)
	info = tuplesToList(cursor.fetchall())
	#a, b, c, d, e = cursor.fetchone()
	#store, orderID, orderDate, orderTime, noItems, quantity = cursor.fetchone()
	return info

def newAss(uname,orderID):
	cursor.execute("select Orderr.order_placed_time, Orderr.delivery_time,deliveredBy.is_delivered, concat(A.house_number,', ',A.street,', ',A.city,', ',A.state,', ',A.state,', ',A.zip_code) ,GroceryStore.store_name from deliveredBy join orderFrom on orderFrom.order_id=deliveredBy.order_id join Orderr on orderFrom.order_id=Orderr.order_id join GroceryStore on orderFrom.store_address_id=GroceryStore.store_id join Address as a on GroceryStore.store_id=A.id where deliveredBy.order_id=%s and deliveredBy.deliverer_username=%s", (orderID, uname))
	orderTime, deliveryTime, isDelivered, address , storeName = cursor.fetchone()
	dictry = {}
	dictry["order_placed"] = orderTime
	dictry["delivery_time"] = deliveryTime
	dictry["status"] = isDelivered
	dictry["address"] = address
	dictry["storeName"] = storeName
	cursor.execute("select Item.item_name,selectItem.quantity from selectItem join Item on Item.item_id=selectItem.item_id where selectItem.order_id =%s", orderID)
	iandq = tuplesToList(cursor.fetchall())
	return dictry, iandq



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
	print(info)
	return info

def addNewPay(uname,payment,accName,routingNo):
    #first check if payment method already exists
    query = "SELECT Count(*) FROM Payments WHERE username = %s AND payment_name = %s"
    cursor.execute(query, (uname,payment))
    payexist = cursor.fetchone()
    cursor.fetchall()
    if payexist != (0,):
        return 1
    query = "INSERT INTO Payments(username, payment_name, account_number, routing_number)"\
    "VALUES (%s,%s,%s,%s);"
    cursor.execute(query, (uname,payment,accName,routingNo))

    conn.commit()
    return 0

def updateDefaultPayment(uname,payment):
    print(payment)
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
	cursor.execute("SELECT Item.item_name, Item.description, Item.quantity, Item.listed_price, Item.wholesale_price, Item.exp_date, Item.item_id From Item Join soldAt on Item.item_id=soldAt.item_id WHERE soldAt.store_id IN (SELECT GroceryStore.store_id FROM GroceryStore Where GroceryStore.address_id IN (SELECT manages.store_address From manages WHERE manages.username=%s)) ",uname)
	#cursor.execute("SELECT Item.item_name, Item.description, Item.quantity, Item.listed_price, Item.wholesale_price, Item.exp_date, From Item Join soldAt on soldAt.item_id = Item.item_id WHERE soldAt.store_id IN (SELECT GroceryStore.store_id FROM GroceryStore Where GroceryStore.address_id IN (SELECT manages.store_address From manages WHERE manages.username=%s) ",uname)
	info =  tuplesToList(cursor.fetchall())
	return info



def outstandingOrders(uname):
	cursor.execute("select GroceryStore.store_name, concat(A.house_number,', ',A.street,', ',A.city,', ',A.state,', ',A.state,', ',A.zip_code), orderFrom.order_id, Orderr.order_placed_date , selectItem.quantity*Item.listed_price, selectItem.quantity, concat(B.house_number,', ',B.street,', ',B.city,', ',B.state,', ',B.state,', ',B.zip_code) from orderFrom natural join Orderr natural join orderedBy natural join selectItem join deliveredby on orderFrom.order_id=deliveredBy.order_id join GroceryStore on GroceryStore.store_id=orderFrom.store_address_id join Buyer on Buyer.username=orderedBy.buyer_username join Address as A on A.id=GroceryStore.store_id join Item on Item.item_id=selectItem.item_id join Address as B on B.id=Buyer.address_id where GroceryStore.address_id in (select store_address from manages where username=%s) and deliveredBy.is_delivered=0",uname)
	info =  tuplesToList(cursor.fetchall())
	return info

def updateDelivery(uname, orderID):
	cursor.execute("update deliveredBy set is_delivered=1,delivery_time=curtime(), delivery_date=curdate() where order_id=%s and deliverer_username=%s", (orderID, uname))
	print("superyeeEET")
	conn.commit()
	return 0

def create_table():
    sql="DROP TABLE IF EXISTS CartView"
    cursor.execute(sql)

    cursor.execute("CREATE TABLE CartView( quantity Int(8) not null, Item_id INT(2) not null)")


def getItemInfo(itemNo):
	cursor.execute(" SELECT Item.item_name, Item.description, Item.quantity, Item.listed_price, Item.wholesale_price, Item.exp_date FROM Item Where Item.item_id = %s " ,itemNo)
	itemName, description, quantity, listedPrice, wholesalePrice, expDate = cursor.fetchone()
	dictry = {}
	dictry["itemName"] = itemName
	dictry["description"] = description
	dictry["quantity"] = quantity
	dictry["listedPrice"] = listedPrice
	dictry["wholesalePrice"] = wholesalePrice
	dictry["expDate"] = expDate
	return dictry

def getOrderInfo(uname,orderID):
	cursor.execute("SELECT GroceryStore.store_name,  Orderr.order_placed_date, SUM(selectItem.quantity*Item.listed_price), COUNT(selectItem.quantity), DeliveredBy.is_delivered FROM GroceryStore Join orderFrom on GroceryStore.store_id=orderFrom.store_address_id Join Orderr on Orderr.order_id=orderFrom.order_id Join selectItem on selectItem.order_id=Orderr.order_id Join Item on Item.item_id=selectItem.item_id join deliveredBy on deliveredBy.order_id=Orderr.order_id join orderedBy on orderedBy.order_id=Orderr.order_id where orderedBy.buyer_username=%s AND Orderr.order_id=%s " , (uname,orderID) )
	storeName, orderDate, totPrice, totItems, deliverer = cursor.fetchone()
	dictry = {}
	dictry["storeName"] = storeName
	dictry["orderDate"] = orderDate
	dictry["totPrice"] = totPrice
	dictry["totItems"] = totItems
	dictry["deliverer"] = deliverer
	return dictry



def popCart():
	cursor.execute("Select Item.item_id,Item.item_name, Item.description, CartView.quantity, CartView.quantity*Item.listed_price, %s from Item join CartView on Item.item_id=CartView.Item_id", "yes")
	info =  tuplesToList(cursor.fetchall())
	return info


def orderTot():
	cursor.execute("Select CartView.quantity*Item.listed_price from Item join CartView on Item.item_id=CartView.Item_id")
	totPrice =  cursor.fetchone()
	return totPrice

def getNewOrderID():
	cursor.execute("SELECT Orderr.order_id FROM Orderr")
	info = tuplesToList(cursor.fetchall())
	print(info)
	return info
