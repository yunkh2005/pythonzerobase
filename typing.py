import random
import time
import winsound
import sqlite3
import datetime

# 본인 DB 파일 경로
conn = sqlite3.connect('C:/Major/Python_workspace/zerobase/records.db', isolation_level=None)

# Cursor연결
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT,  cor_cnt INTEGER, record text, regdate text)')

words = []       # 영어 단어 리스트
n = 1           # 게임 시도 횟수
cor_cnt = 0     # 정답 개수

with open('C:/Major/Python_workspace/zerobase/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())
# print(words)    # 단어 리스트 확인

input("Ready? press Enter Key!")

start = time.time()

while n <= 5:
    random.shuffle(words)
    q = random.choice(words)

    print()

    print("*Question # {}".format(n))
    print(q)        # 문제 출력

    x = input()    # 정답 입력
    print()
    
    if str(q).strip() == str(x).strip():
        print("Pass!")
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        cor_cnt += 1
    else:
        print("Wrong...!")
        winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
    n += 1

end = time.time()   # 게임 종료 시간 측정
et = end - start    # 총 시간 측정
et = format(et, ".3f")

if cor_cnt >3:
    print("합격입니다.")
else:
    print("불합격입니다.")

# DB
cursor.execute("INSERT INTO records('cor_cnt', 'record', 'regdate') VALUES (?, ?, ?)", (cor_cnt, et, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

conn.close()

# 총 시간 출력
print("게임시간: ", et, "초 ", "정답 개수: {}".format(cor_cnt))
