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
        string = string.replace(' ', '')
        for str in string:
            if str == '+':
                self.stack.push(self.stack.pop() + self.stack.pop())
            elif str == '-':
                num = self.stack.pop()
                self.stack.push(self.stack.pop() - num)
            elif str == '*':
                self.stack.push(self.stack.pop() * self.stack.pop())
            elif str == '/':
                num = self.stack.pop()
                self.stack.push(self.stack.pop() // num)
            else:
                self.stack.push(int(str))
        return self.stack.pop()

# Test code
calc = Calculator()
print(calc.calculate('4 6 * 2 / 2 +'))          # 답: 14
print(calc.calculate('2 5 + 3 * 6 - 5 *'))      # 답: 75