import mysql.connector
from pymysql import *



'''#host=
#user=
#password=
#----->closinng the database
#insert
#----->executed
#----->closinng the db(commit)
#print'''

insertdata = mysql.connector.connect(host='localhost',user='root',password='',database='insertfrompy')
mycursor=insertdata.cursor()

sql="INSERT INTO insertion (name,address,age) VALUES ('%s','%s',%d)"
value=("player1","southwest",67)
mycursor.execute(sql,value)

insertdata.commit()
print(mycursor.rowcount,'record inserted')


con=connect(host='locallhost')
