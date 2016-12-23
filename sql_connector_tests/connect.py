import mysql.connector
from mysql.connector import errorcode

default_user = 'root'
default_password = 'coupang@123'
default_host = '127.0.0.1'
default_port = 3306

def connect():
    cnx = mysql.connector.connect(user=default_user, password=default_password,
                                host=default_host, port=default_port,
                                database='employees')
    cnx.close()


#To handle connection errors, use the try statement and catch all errors using the errors.Error exception:
def connect_handle_error(database_name):
    try:
        cnx = mysql.connector.connect(user=default_user, password=default_password,
                                host=default_host, port=default_port,
                                database=database_name)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()


#If you have lots of connection arguments, it's best to keep them in a dictionary and use the ** operator:
config = {
    'user': 'root',
    'password': 'coupang@123',
    'host': '127.0.0.1',
    'database': 'employees',
    'raise_on_warnings': True,
    'use_pure': False,
}

def connect_config(config):
    cnx = mysql.connector.connect(**config)
    cnx.close()


if __name__ == '__main__':
    #connect_handle_error('employees')
    connect_config(config)