import pymysql

conn = pymysql.connect(host="localhost",
							db="GroceryTech",
							user="root",
							passwd='password')
cursor = conn.cursor()
'''comment'''
