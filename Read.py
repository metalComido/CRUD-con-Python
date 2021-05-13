import sqlite3

#Connect to data base
connection = sqlite3.connect('DB\PythonStudents.db')

#Create a cursor
Consult = connection.cursor()


Consult.execute("SELECT rowid, * FROM StudentsList")

items = Consult.fetchall()

print("id"+"\tEnrollment"+"\t\tFirst Name"+"\t\tLast Name")
print("-"+"\t----------"+"\t\t---------"+"\t\t-----------")
for item in items:
    print(item[0],"\t",item[1],"\t\t",item[2],"\t\t",item[3])

connection.commit()

connection.close()