import sqlite3

conn = sqlite3.connect('C:/Major/Python_workspace/zerobase/database.db')

c = conn.cursor()

c.execute("SELECT * FROM users")

# print('One -> \n', c.fetchone())

# print('Three -> ')

# rows = c.fetchall()
# for row in rows:
#     print('retrieve1 > ', row)

# for row in c.fetchall():
#     print('retrieve2 > ', row)

# for row in c.execute('SELECT * FROM users ORDER BY id desc'):
#     print(row)

param1 = (3,)
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1: ', c.fetchall())

param2 = (4,)
c.execute('SELECT * FROM users WHERE id="%s"' % param2)
print('param2: ', c.fetchone())