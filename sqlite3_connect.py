import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

# delete table
c.execute('DROP TABLE IF EXISTS users')

# create table
c.execute('''
	CREATE TABLE IF NOT EXISTS users(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT,
		age INTEGER)
''')

# insert table
rows = [('David', 45),('Christophe', 56)]
c.executemany('INSERT INTO users(name, age) VALUES (?, ?)', rows)

# select
try:
	c.execute('SELECT name, age FROM users')
except:
	print('SQLite Error')
else:
	for enreg in c:
		print(enreg)

conn.commit()

conn.close()
