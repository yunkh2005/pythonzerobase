'''
과제2.
아래 기반 코드를 완성하여, 입력받은 값 중 중앙값을 출력하는 클래스를 완성하시오. 입력받은 값이 짝수개이면, 중앙값 2개의 평균을 출력하시오. (단, clear 메소드는 입력받은 내역을 모두 삭제)

class Median:
    def __init__(self):
        pass

    def get_item(self, item):
        pass

    def clear(self):
        pass

    def show_result(self):
        pass

median= Median()
for x in range(10):
    median.get_item(x)
median.show_result()

median.clear()
for x in [0.5, 6.2, -0.4, 9.6, 0.4]:
    median.get_item(x)
median.show_result()

출력
4.5
0.5
'''

class Median:
  def __init__(self):
      self.list = list()
  def get_item(self, item):
      self.list.append(item)
  def clear(self):
      self.list = list()
  def show_result(self):
      self.list.sort()
      n = len(self.list)
      if n % 2 == 1:
          med = self.list[n // 2]
      else:
          med = (self.list[n // 2 - 1] + self.list[n // 2]) / 2
      print(med)
median= Median()
for x in range(10):
  median.get_item(x)
median.show_result()
median.clear()
for x in [0.5, 6.2, -0.4, 9.6, 0.4]:
  median.get_item(x)
median.show_result()