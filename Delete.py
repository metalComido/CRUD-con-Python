import sqlite3

#Connect to data base
connection = sqlite3.connect('DB\PythonStudents.db')

#Create a cursor
Consult = connection.cursor()

#Deleting in database PythonStudents
Consult.execute("DELETE FROM StudentsList WHERE rowid = 2")

connection.commit()

connection.close()
