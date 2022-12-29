'''
과제1.
다음과 같이 작성된 csv 파일을 읽고, 읽어들인 모든 값을 더해서 출력하는 파이썬 프로그램을 작성하시오.
csv파일의 위치는 실행 위치와 동일하다고 가정한다. 즉, open('a.csv', 'r')으로 파일을 열 수 있다. csv 파일에 담긴 내용은 달라질 수 있으며, 자료의 개수는 10000개 이하이다.

- a.csv에 작성된 내용
10,60,20,33,55,25,64,83,523,54,87,84,56,84

출력
1238
'''

import csv
sum = 0
with open('a.csv', 'r') as f:
  reader = csv.reader(f)
  for line in reader:
      for elem in line:
          sum += int(elem)
print(sum)