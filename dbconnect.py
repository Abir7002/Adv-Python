import mysql.connector as mc

db = mc.connect(user="alone",password="alone",host="localhost")

mydb = db.cursor()
query = input("enter your query")
mydb.execute(query)

data = mydb.fetchall()

for x in data:
    print(x)
