import sqlite3


connection=sqlite3.connect('student.db')

## Create a cursor object using the connection to insert or create tables
cursor = connection.cursor()


## create a table
table_info = """
create table STUDENT (NAME VARCHAR(25  ),CLASS VARCHARN(25),
SECTION VARCHAR(25),MARKS INT)
"""


cursor.execute(table_info)

## Insert some more records
cursor.execute("INSERT INTO STUDENT VALUES('Tiwri', 'data science', 'A', 95)")
cursor.execute("INSERT INTO STUDENT VALUES('John', 'devops', 'B', 85)")
cursor.execute("INSERT INTO STUDENT VALUES('mukesh', 'dat science', 'A', 80)")
cursor.execute("INSERT INTO STUDENT VALUES('jacob', 'devops', 'A', 75)")
cursor.execute("INSERT INTO STUDENT VALUES('krish', 'data science', 'A', 90)")


## Display all the records
print("the inserted records are:")
data=cursor.execute('''SELECT * FROM STUDENT''')

for row in data:
    print(row)
    
## commit you changes in the database
connection.commit()
connection.close()