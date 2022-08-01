import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

# Inserting One Record at a Time
c.execute("INSERT INTO customers VALUES ('Mary', 'Blow', 'mb@test.com')")

# Inserting multiple records at once:

many_customers = [
    ('Wes', 'Brown', 'wb@example.com'),
    ('Stephanie', 'Brown', 'sb@example.com'),
    ('Harry', 'Potter', "hp@hogwarts.com")
]

c.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customers)

conn.commit()
conn.close()