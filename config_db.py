import mysql.connector

def getDB():

    flaskDB = mysql.connector.connect(
        host='',
        user='',
        password='',
        database='',
        auth_plugin='mysql_native_password'
    )
    return flaskDB
