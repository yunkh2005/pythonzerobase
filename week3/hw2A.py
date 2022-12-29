'''
과제 2.

아래는 Python의 list를 이용하여 Stack을 구현한 것이다. 
Stack의 특성을 이용하면 후위 표기법으로 작성된 수식을 계산할 수 있다. 
후위 표기법은 연산자를 나중에 표기하는 표기법으로, 아래와 같이 계산한다. 
후위 표기법에서 사칙연산의 우선순위는 없다고 가정한다.
10 5 + 2 * 3 /
= 15 2 * 3 /
= 30 3 /
= 10
연산자와 피연산자가 공백으로 구분된다고 할 때, 
내부적으로 stack을 유일한 자료구조로 사용하여 후위 표기법으로 표기된 수식을 계산하여 반환하는 메소드 calculate()을 완성하시오.

class Stack:
    def __init__(self):
        self.list = list()

    def push(self, data):
        self.list.append(data)

    def pop(self):
        return self.list.pop()

class Calculator:
    def __init__(self):
        self.stack = Stack()

    def calculate(self, string):
        pass

# Test code
calc = Calculator()
print(calc.calculate('4 6 * 2 / 2 +'))
print(calc.calculate('2 5 + 3 * 6 - 5 *'))
'''

class Stack:
  def __init__(self):
      self.list = list()

  def push(self, data):
      self.list.append(data)

  def pop(self):
      return self.list.pop()
class Calculator:
  def __init__(self):
      self.stack = Stack()

  def calculate(self, string):
      for x in string.split(' '):
          if x == '+':
              self.stack.push(self.stack.pop() + self.stack.pop())
          elif x == '-':
              self.stack.push(- self.stack.pop() + self.stack.pop())
          elif x == '*':
              self.stack.push(self.stack.pop() * self.stack.pop())
          elif x == '/':
              self.stack.push(1 / self.stack.pop() * self.stack.pop())
          else:
              self.stack.push(int(x))
      return self.stack.pop()   
calc = Calculator()
print(calc.calculate('4 6 * 2 / 2 +'))
print(calc.calculate('2 5 + 3 * 6 - 5 *'))