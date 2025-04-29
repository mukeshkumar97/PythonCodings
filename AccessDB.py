import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="mukesh", passwd="mukesh@1997")

#We can also add the database in the connector like below line
#mydb2 = mysql.connector.connect(host="localhost", user="mukesh", passwd="mukesh@1997", database="mkdatabase")
mycursor = mydb.cursor()
mycursor.execute("show databases")
#Display the databases
for i in mycursor:
    print(i)

mycursor2 = mydb.cursor()
mycursor2.execute("select * from mkdatabase.student")
#Display data in table
#for i in mycursor2:
#    print(i)

#We can also store the result in a variable and print like below:
result = mycursor2.fetchall()
for i in result:
    print(i)