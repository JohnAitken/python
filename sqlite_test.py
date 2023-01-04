import sqlite3
#https://www.youtube.com/watch?v=pd-0G0MigUA&t=191s
#Connect to the db, will create the .db file if it is not there
conn = sqlite3.connect("test.db")

#create a cursor to allow for us to query this db with the EXECUTE method.
c = conn.cursor()

#use execute method to do your SQL statement. """ denotes multiple lines of code. single quotes for a single line of code
# c.execute("""
# CREATE TABLE users (id INTEGER NOT NULL PRIMARY KEY, name TEXT NOT NULL, email TEXT)
# """)

#To add data to the created table
# c.execute("INSERT INTO users VALUES(3,'Clive','Fsgfd@fgdsd,com')")

#To query the db
c.execute("SELECT * FROM Users")
print(c.fetchall())

#




#commit the connection (not the cursor) which completes the transaction, then close
conn.commit()
conn.close()