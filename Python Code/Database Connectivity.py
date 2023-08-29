# Database Connectivity


import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="root")

mycursor = mydb.cursor()

mycursor.execute("show databases")

for i in mycursor:
    print(i)
