a = ['base ball', 'basket ball', 'soccer', 'base ball', 'soccer', 'soccer', 'basket ball', 'base ball', 'basket ball', 'soccer', 'basket ball', 'basket ball', 'base ball', 'soccer', 'soccer', 'basket ball', 'basket ball', 'base ball', 'base ball']
cloneA = list(set(a))   # 스포츠 종목 추출
afterClass = dict.fromkeys(cloneA, 0)   # 스포츠 종목명 딕셔너리 key로 저장

for i in range(len(a)):
    for j in range(len(cloneA)):
        if cloneA[j] == a[i]:
            afterClass[cloneA[j]] += 1

# 딕셔너리 출력
for key, value in afterClass.items():
    print(key, value)
