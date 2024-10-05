import sqlite3

con = sqlite3.connect("SQLiteMagic.db")
cur = con.cursor()

cur.execute('''SELECT * FROM INTERNATIONAL_STUDENT_TEST_SCORES''')
print(cur.fetchall())

con.commit()


