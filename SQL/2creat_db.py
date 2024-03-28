import mysql.connector

myDB = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "004962"
)

myCursor = myDB.cursor()
myCursor.execute("CREATE DATABASE myfirstDB")

myCursor.execute("SHOW DATABASES")

for x in myCursor:
    print(x)