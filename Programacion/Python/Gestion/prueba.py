import sqlite3

con = sqlite3.connect("Sql.db")
cur = con.cursor()

cur.execute("SELECT * FROM productos WHERE id = 3")

print(cur.fetchall())
