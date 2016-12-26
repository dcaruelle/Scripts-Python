import sqlite3

conn = sqlite3.connect('ma_base.db')

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXIST users(
  id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
  name TEXT,
  age INTEGER
)
""")
conn.commit()

cursor.execute("""
INSERT INTO users(name, age) VALUES(?, ?)""", ("David", 45))

db.close