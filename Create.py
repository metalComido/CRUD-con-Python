import sqlite3

#Connect to data base
connection = sqlite3.connect('DB\PythonStudents.db')

#Create a cursor
Consult = connection.cursor()

many_Students = [
                    ('01223402','leobardo','Sanchez'),
                    ('01234567','prueba','python'),
                    ('98765432','pruebas2','python2'),
                ]

Consult.executemany("INSERT INTO StudentsList VALUES (?,?,?)", many_Students)

print('command execute succesfully...')

connection.commit()

connection.close()