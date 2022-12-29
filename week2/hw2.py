num = []
class Median:
    def __init__(self):
        pass

    def get_item(self, item):
        self.item = item
        num.append(item)

    def clear(self):
        num.clear()

    def show_result(self):
        num.sort()                      # 리스트 정렬
        center = len(num) // 2          # 중간 인덱스 변수 생성
        # 입력 받은 값이 짝수일 때
        if len(num) % 2 == 0:
            print((num[center - 1] + num[center]) / 2)
        # 입력 받은 값이 홀수일 때
        else:
            print(num[center])

median= Median()
for x in range(10):
    median.get_item(x)
median.show_result()

median.clear()
for x in [0.5, 6.2, -0.4, 9.6, 0.4]:
    median.get_item(x)
median.show_result()