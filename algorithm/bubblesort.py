import random

def bubble(data):
    for i in range(len(data) - 1):
        for j in range(1, len(data) - i):
            check, swap = 0, 0
            if data[j-1] > data[j]:
                data[j-1], data[j] = data[j], data[j-1]
                check += 1
            else:
                continue
        
            if check == 0:
                break
        
    
    return data


data = random.sample(range(100), 10)
print("before:", data)
print ("after", bubble(data))

'''
버블 정렬(Bubble Sort)
- 두 인접한 데이터를 비교해, 앞에 있는 데이터가 뒤에 있는 데이터보다 크면,
  자리를 바꾸는 정렬 알고리즘
- 리스트 안 n개가 있는 경우 최대 n-1번의 로직을 적용
- 로직을 1번 적용할 때마다 가장 큰 숫자가 뒤에서부터 1개씩 결정
- 로직 적용중 한번도 데이터가 교환되지 않았다면,
  이미 정렬된 상태이므로 로직을 반복 적용할 필요가 없음
- O(n^2): 반복문이 두개이므로
- O(n): 최선, 완전 정렬이 되어있는 경우
'''