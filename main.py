import sqlite3, datetime

now = datetime.datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
conn = sqlite3.connect('C:/Major/Python_workspace/zerobase/database.db', isolation_level=None)

c = conn.cursor()
print('Cursor Type : ', type(c))

# 테이블 생성(Datatype : TEXT NUMERIC INTEGER REAL BLOB)
c.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    username text, email text,
    phone text,
    website text, 
    regdate text)''')  # AUTOINCREMENT

# 데이터 삽입
#c.execute("INSERT INTO users VALUES (1 ,'Kim','Kim@naver.com', '010-0000-0000', 'Kim.com', ?)", (nowDatetime,))
#c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)",
#          (2, 'Park', 'Park@naver.com', '010-1111-1111', 'Park.com', nowDatetime))

# Many 삽입(튜플, 리스트)
# userList = (
#     (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDatetime),
#     (4, 'Cho', 'Cho@naver.com', '010-3333-3333', 'Cho.com', nowDatetime),
#     (5, 'Yoo', 'Yoo@naver.com', '010-4444-4444', 'Yoo.com', nowDatetime)
# )
# c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", userList)