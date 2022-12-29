# 1. 아래 문자열의 길이를 구해보세요.
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print(len(q1))

print()
# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon
print('apple;orange;banana;lemon')

print()
# 3. 화면에 * 기호 100개를 표시하세요.
print('*' * 100)

print()
# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.
print(type(int("30")), type(float("30")), type("30"))

print()
# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.
str = "Niceman"
print(str[4:])

print()
# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"
str = "Strawberry"
print(str[::-1])

print()
# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"
num = "010-7777-9999"
print(num.replace("-", ""))

print()
# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"
url = "http://daum.net"
print(url.replace("http://", "www."))

print()
# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"
str = "Niceman"
print("대문자: ", str.upper())
print("소문자: ", str.lower())

print()
# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"
str = "abcdefghijklmn"
print(str[2:5])

print()
# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
a = ["Banana", "Apple", "Orange"]
a.remove("Apple")
print(a)

print()
# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)
tuple = (1,2,3,4)
list = list(tuple)
print(type(list))

print()
# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. 
# <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
dict = {
    "성인" : 100000,
    "청소년" : 7000,
    "아동" : 3000
}
for k, v in dict.items():
    print(k, v)

print()
# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
dict["소아"] = 0
for k, v in dict.items():
    print(k, v)

print()
# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
for k in dict.keys():
    print(k)

print()
# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
for v in dict.values():
    print(v)