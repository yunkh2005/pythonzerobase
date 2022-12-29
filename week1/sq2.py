# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
print(q1["가을"])

print()
# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for i in q2.values():
    if i == "사과":
        print("있습니다.")

print()
# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
grade = 40
if grade >= 81:
    print("A")
elif grade >= 61:
    print("B")
elif grade >= 41:
    print("C")
elif grade >= 21:
    print("D")
else:
    print("F")

print()
# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
a = 12
b = 6
c = 18
if a > b and a > c:
    print("a")
elif b > a and b > c:
    print("b")
else:
    print("c")

print()
# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
admin = "2111111"
if admin[0] == "2" or admin[0] == "4":
    print("female")
else:
    print("male")

print()
# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]
for i in q3:
    if i == "정":
        continue
    print(i, end="")

print()
print()
# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
for i in range(1, 100 + 1):
    if i % 2 != 0 :
        print(i, end=" ")

print()
print()
# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
for i in q4:
    if len(i) >= 5:
        print(i)

print()
# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for i in q5:
    if i == i.lower():
        print(i)

print()
# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for i in q6:
    if i == i.lower():
        print(i.upper())
    else:
        print(i.lower())
    