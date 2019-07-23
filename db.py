import pymysql

conn = pymysql.connect(host="localhost",
							db="GroceryTech",
							user="root",
							passwd='CornyJoke12')
cursor = conn.cursor()

# returns 0 if credentials are invalid
# returns 1 if user is a manager
# returns 2 if user is NOT a manager
def login(username, password):
    query = "SELECT COUNT(*) FROM userr WHERE username = %s AND password = %s;"
    response = cursor.execute(query, (username, password))
    # clear cursor
    cursor.fetchall()

    if response == 0:
        return 0
    else:
        query = "SELECT user_type FROM userr WHERE username = %s;"
        response = cursor.execute(query, (username))

        result = cursor.fetchone()

        # sanity check
        cursor.fetchall()

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
    cursor.commit()

def systeminfo(sysID,code):
    query = "SELECT COUNT(user_codes) FROM SystemInformation WHERE user_codes=%s"
    cursor.execute(query, code)
    for i in cursor:
        response = i[0]
    #return cursor
    cursor.fetchall()
    if response != 1:
        query = "INSERT INTO SystemInformation(system_id,user_codes)"\
        "VALUES (%s,%s);"
        cursor.execute(query, (sysID,code))
        conn.commit()
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
	cursor.execute("SELECT * FROM Addresses Where address_id=%s",address)
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
	
	
	
	return dictry

