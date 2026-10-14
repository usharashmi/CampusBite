import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="Usha@321",
    database="campusbite"
)

print("Connected Successfully")