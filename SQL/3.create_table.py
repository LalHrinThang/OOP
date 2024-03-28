import mysql.connector

myDB_connection = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="004962"
)

myCursor = myDB_connection.cursor()

myCursor.execute("CREATE DATABASE TableCreation")
myCursor.execute("SHOW DATABASES")

for database in myCursor:
    print(database)