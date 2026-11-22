import mysql.connector

# Connect directly to your existing database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_program"
)
cur = conn.cursor()
print("Connected to python_program database successfully")

# CREATE TABLE
cur.execute("DROP TABLE IF EXISTS student")
cur.execute("""CREATE TABLE student (
                 id INT PRIMARY KEY,
                 name VARCHAR(50),
                 marks INT)""")

# INSERT
cur.execute("INSERT INTO student VALUES (1, 'Amit', 78)")
cur.execute("INSERT INTO student VALUES (2, 'Riya', 85)")
cur.execute("INSERT INTO student VALUES (3, 'Karan', 62)")
conn.commit()
print("Records inserted")

# UPDATE
cur.execute("UPDATE student SET marks = 90 WHERE id = 3")

# DELETE
cur.execute("DELETE FROM student WHERE id = 1")
conn.commit()

# SELECT
cur.execute("SELECT * FROM student")
print("Records after update and delete:")
for row in cur.fetchall():
    print(row)

cur.close()
conn.close()