import mysql.connector

dbConnection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "004962",
    database = "TableCreation"
)


dbcursor = dbConnection.cursor()
#dbcursor.execute("CREATE TABLE students(id int primary key AUTO_INCREMENT,name VARCHAR(30),age SMALLINT,class TINYINT)")

#dbcursor.execute("ALTER TABLE students ADD hobby VARCHAR(30)")

insert_data_type= "INSERT INTO students (id,name,age,class,hobby)values(%s,%s,%s,%s,%s)"

insert_data = [(101,"Lal Hrin Thang",24,12,"Programming"),(102,"Lal Hrin Thang",24,12,"Programming"),(103,"Lal Hrin Thang",24,12,"Programming")]
dbcursor.executemany(insert_data_type,insert_data)

print("Data successfully inserted")
print(dbcursor.rowcount)

dbcursor.execute("SELECT * FROM students")
for i in dbcursor:
    print(i)