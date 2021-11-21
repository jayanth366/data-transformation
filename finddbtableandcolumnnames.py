import sqlite3
  
# Connecting to sqlite
conn = sqlite3.connect('cma-artworks.db')
  
# Creating a cursor object using the cursor() method
cursor = conn.cursor()
  
  
# Display columns
print('\nColumns in creator table:')
data=cursor.execute('''SELECT * FROM creator''')
for column in data.description:
    print(column[0])

print('\nColumns in artwork table:')
data=cursor.execute('''SELECT * FROM artwork''')
for column in data.description:
    print(column[0])

print('\nColumns in artwork__department table:')
data=cursor.execute('''SELECT * FROM artwork__department''')
for column in data.description:
    print(column[0])
      
# Display data
print('\nData in creator table:')
data=cursor.execute('''SELECT * FROM creator''')
for row in data:
    print(row)
      
# Commit your changes in the database    
conn.commit()
  
# Closing the connection
conn.close()