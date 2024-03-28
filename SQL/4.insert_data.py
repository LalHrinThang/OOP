import mysql.connector

dbConnection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "004962",
    database = "TableCreation"
)


dbcursor = dbConnection.cursor()
#dbcursor.execute("CREATE TABLE students(id int primary key AUTO_INCREMENT,name VARCHAR(30),age SMALLINT,class TINYINT)")

dbcursor.execute("ALTER TABLE students ADD hobby VARCHAR(30)")


dbcursor.execute("DESCRIBE students")

for i in dbcursor:
    print(i)