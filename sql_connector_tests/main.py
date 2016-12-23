import mysql.connector

cnx = mysql.connector.connect(user='root', password='coupang@123',
                              host='127.0.0.1', port=3306,
                              database='employees')
cnx.close()