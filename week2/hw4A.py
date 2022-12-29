'''
과제4.
아래 기반 코드를 완성하여, 주어진 출력을 하는 클래스를 구현하시오. 기반 코드에 제시된 대로 print문 하나당 문자 하나씩만 출력하시오.

class Foo:
    pass

print(Foo.bar)       # A 출력
print(Foo().bar)     # B 출력
print(Foo.Bar.bar)   # C 출력
print(Foo.Bar().bar) # D 출력

출력
A
B
C
D

'''

class Bar:
    bar = 'C'
    def __init__(self):
        self.bar = 'D'