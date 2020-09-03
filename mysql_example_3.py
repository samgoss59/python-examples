import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="samuel",
    passwd="Matt@vw2015",
    database="sakila"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT last_name FROM actor")
myresult = mycursor.fetchone()
for row in myresult:
    print(row)
    

