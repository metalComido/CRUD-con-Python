import sqlite3

#Connect to data base
connection = sqlite3.connect('DB\PythonStudents.db')

#Create a cursor
Consult = connection.cursor()

#updating data from database StudentList using Firstname
Consult.execute("""UPDATE StudentsList SET FirstName = 'Jose'
                    WHERE FirstName = 'prueba'
                
                """)


connection.commit()

connection.close()