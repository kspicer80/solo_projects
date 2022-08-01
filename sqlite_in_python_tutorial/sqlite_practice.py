import sqlite3

conn = sqlite3.connect('customers.db')

c = conn.cursor()

# Creating the Table:
#c.execute("""CREATE TABLE customers(
    #first_name text,
    #last_name text,
    #e_mail text)""")

# Inserting a Single Record into the Database
'''
c.execute("INSERT INTO customers VALUES ('Mary', 'Blow', 'mb@test.com')")

# Inserting multiple records at once:
many_customers = [
    ('Hermione', 'Granger', 'hg@hogwarts.com'),
    ('Ronald', 'Weesley', 'rw@hogwarts.com'),
    ('Harry', 'Potter', "hp@hogwarts.com")
]

c.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customers)
'''

# Querying the Database
#c.execute("SELECT * FROM customers")
#c.execute("SELECT rowid, * FROM customers")
#c.execute("SELECT * FROM customers WHERE last_name = 'Granger'")
#c.execute("SELECT * FROM customers WHERE last_name LIKE 'Wee%'")
#c.execute("SELECT * FROM customers WHERE e_mail LIKE '%hogwarts.com'")
#print(c.fetchone()) # fetch one
#c.fetchmany(2) # fetch two 
#print(c.fetchall()) # fetch all

# How do we update records ...?
#c.execute("""UPDATE customers SET first_name = 'Joe'
 #           WHERE rowid=1
  #          """)
#conn.commit()

# How do we delete records ...?
#c.execute("DELETE from customers WHERE rowid = 1")

#c.execute("SELECT rowid, * FROM customers")
#c.execute("SELECT rowid, * FROM customers")


#print("NAME " + "\t\tEMAIL")
#print("----" + "\t\t-----" )
#for item in items:
    #print(item[0] + " " + item[1] + " " + item[2])

# Ordering Results
c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")
items = c.fetchall()
for item in items:
    print(item)

# Searching for Specific Things
print("Commands executed successfully ...")
conn.commit()
conn.close()
