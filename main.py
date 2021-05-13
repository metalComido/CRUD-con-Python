import sqlite3
from sqlite3.dbapi2 import connect

#Connect to data base
connection = sqlite3.connect('PythonStudents.db')

#Create a cursor
Consult = connection.cursor()

#Create table
Consult.execute("""CREATE TABLE IF NOT EXISTS StudentsList (
        Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        enrollment INTEGER,
        FirstName VARCHAR(60) NOT NULL,
        LastName VARCHAR(60) NOT NULL,
            
    )""")
