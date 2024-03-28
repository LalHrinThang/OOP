import mysql.connector

myDB_connection = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="004962",
    database ="TableCreation"
)

myCursor = myDB_connection.cursor()

#myCursor.execute("CREATE TABLE FirstTB(id int primary key AUTO_INCREMENT,name VARCHAR(30),age SMALLINT,class TINYINT)")

myCursor.execute("DESCRIBE FirstTB")
for database in myCursor:
    print(database)