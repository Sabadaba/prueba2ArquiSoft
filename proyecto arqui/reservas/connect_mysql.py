#pip install mysql-connector-python==8.0.29
import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password='',
  port=3306
)

cur = conn.cursor()

cur.execute("SHOW DATABASES")

for row in cur:
  print(row) 

cur.execute("CREATE DATABASE db_reservas")
