class Foo():
    bar='A'
    def __init__(self):
        self.bar='B'

    class Bar():
        bar='C'
        def __init__(self):
            self.bar='D'
        
print(Foo.bar)       # A 출력, Foo클래스 bar변수 출력
print(Foo().bar)     # B 출력, Foo클래스의 상속자에서 bar변수 출력
print(Foo.Bar.bar)   # C 출력, Foo클래스 내 Bar클래스에서 bar변수 출력
print(Foo.Bar().bar) # D 출력 Foo클래스 내 Bar클래스의 상속자에서 bar변수 출력