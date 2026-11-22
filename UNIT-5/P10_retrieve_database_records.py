import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_program"
)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS emp")
cur.execute("CREATE TABLE emp (id INT, name VARCHAR(50), salary INT)")

cur.executemany("INSERT INTO emp VALUES (%s, %s, %s)", [
    (1, "Amit", 30000),
    (2, "Riya", 40000),
    (3, "Karan", 35000),
    (4, "Neha", 45000),
    (5, "Raj", 38000)
])
conn.commit()

cur.execute("SELECT * FROM emp ORDER BY id")

# fetchone() - gets one record
print("fetchone:", cur.fetchone())

# fetchmany() - gets the given number of next records
print("fetchmany(2):", cur.fetchmany(2))

# fetchall() - gets all remaining records
print("fetchall (remaining):")
for row in cur.fetchall():
    print(row)

cur.close()
conn.close()