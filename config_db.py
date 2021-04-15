import mysql.connector

def getDB():

    flaskDB = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Pirple',
        database='flask_pirple',
        auth_plugin='mysql_native_password'
    )
    return flaskDB