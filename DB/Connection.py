import sqlite3

#Connect to data base
connection = sqlite3.connect('DB\PythonStudents.db')

#Create a cursor
Consult = connection.cursor()
#Create table
Consult.execute("""CREATE TABLE IF NOT EXISTS StudentsList (
        enrollment INTEGER,
        FirstName VARCHAR(60) NOT NULL,
        LastName VARCHAR(60) NOT NULL
    )""")

#Commit our command
connection.commit()

#Close out connection
connection.close()