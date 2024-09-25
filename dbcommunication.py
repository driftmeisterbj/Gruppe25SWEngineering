import mysql.connector as dbc

mydb = dbc.connect(
    host="localhost",
    user="root",
    password="123"
)

print(mydb)