'''
과제3.
아래 기반 코드를 완성하여, 주어진 출력을 하는 클래스를 구현하시오. 단, Animal 클래스는 수정하지 않고 구현하시오. 최소한의 메소드만을 추가하여 구현하시오. 하나의 메소드는 하나의 line만을 출력하시오.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' cannot speak.')

    def move(self):
        print(self.name + ' cannot move.')


class Dog(Animal):
    pass


class Retriever(Dog):
    pass


dog = Dog('Nancy')
dog.speak()
dog.move()

super_dog = Retriever('Michael')
super_dog.speak()
super_dog.move()

출력
Nancy cannot speak.
Nancy moves like a jagger.
Michael is smart enough to speak.
Michael moves like a jagger.
'''

class Animal:
  def __init__(self, name):
      self.name = name
  def speak(self):
      print(self.name + ' cannot speak.')
  def move(self):
      print(self.name + ' cannot move.')