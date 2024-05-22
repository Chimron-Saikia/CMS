import mysql.connector # type: ignore

dataBase=mysql.connector.connect(
    host='localhost',
    user='root' ,
    passwd='Chim@1234'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")