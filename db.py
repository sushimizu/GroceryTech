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
    query = "INSERT INTO Userr(uname,password,user_type,email,fname,lname)"\
    "VALUES (%s,%s,%s,%s,%s);"
    try:
        response = _cursor.execute(query, (uname,password,user_type,email,fname,lname))
        _database.commit()

        return 0

    except Exception as e:
        if e[1][-2:] == 'Y\'':  # violates primary key constraint, username
            return 1
        '''else:
            return 2'''

def insertBuyer(Username, Phone, AddressID, DefaultPayment, DefaultStoreID):
    query = "INSERT INTO Buyer(username, phone, address_id, default_payment, default_store_id)"\
    "VALUES (%s,%d,%d,%s,%d);"
    response = _cursor.execute(query, (Username, Phone, AddressID, DefaultPayment, DefaultStoreID))

    _database.commit()


def insertAddress(AddID,house_num,street,state,city,zipp):
    query = "INSERT INTO Address(AddID,house_num,street,state,city,zipp)"\
    "VALUES (%d,%d,%s,%s,%s,%d);"
    response = cursor.execute(query, (AddID,house_num,street,state,city,zipp))
    # clear cursor
    cursor.fetchall()

