import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="samuel",
    passwd="Matt@vw2015",
    database="sakila"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM actor")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)
    

