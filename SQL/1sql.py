import mysql.connector

myDB = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "004962"
)

connectionDB = myDB.cursor()

connectionDB.execute("SHOW DATABASES")
for i in connectionDB:
    print(i)