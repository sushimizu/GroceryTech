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



def insertBuyer(Username, Phone, AddressID, DefaultPayment, DefaultStoreID):
	query = "INSERT INTO Buyer (username, phone, address_id, default_payment, default_store_id) VALUES(%s,%d,%d,%s,%s)"
	cursor.execute(query, )
