import pymysql

conn = pymysql.connect(host="localhost",
							db="GroceryTech",
							user="root",
							passwd='password')
cursor = conn.cursor()



def insertBuyer():
	query = "INSERT INTO Buyer (username, phone, address_id, default_payment, default_store_id) VALUES(%s,%d,%d,%s,%s)"
	cursor.execute()
