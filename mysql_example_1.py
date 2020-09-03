import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Matt@vw2015"
)    

print( mydb)