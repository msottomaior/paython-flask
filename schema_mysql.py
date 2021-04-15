import mysql.connector

flaskDB = mysql.connector.connect(
  host='127.0.0.1',
  user='root',
  password='Pirple',
  database='flask_pirple',
  auth_plugin='mysql_native_password'
)

mycursor = flaskDB.cursor()

# mycursor.execute("CREATE DATABASE flask_pirple")
mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(16), pass VARCHAR(16), name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("CREATE TABLE todo (id INT AUTO_INCREMENT PRIMARY KEY, user_id INTEGER, FOREIGN KEY(user_id) REFERENCES users(id), task VARCHAR(255) NOT NULL, from_date date NOT NULL)")
