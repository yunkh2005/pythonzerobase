'''
과제 4
마을에 1부터 N의 고유 번호를 가진 사람들이 있다. 
소문으로는 마을 사람 중에 마을 판사가 있다고 한다. 
마을 판사가 실제로 존재한다면, 마을 판사는 아무도 믿지 않는다.
다른 모든 사람들은 마을 판사를 믿는다.
마을 판사가 있다면 오직 한명 뿐이다.
리스트 trust가 주어졌을 때, trust[i] = [a, b]는 
고유 번호가 a인 사람이 고유 번호가 b인 사람을 믿는다는 것을 의미한다고 한다.
마을 판사가 존재한다면 마을 판사의 고유 번호를, 
존재하지 않는다면 -1을 출력하는 프로그램을 작성하시오.
(단, a가 b를 믿고 b가 c를 믿는다고 할 때, 
a가 c를 믿는다는 의미는 아니다.)

예시입력
N	trust	                            출력
2	[[1,2]]	                            2
3	[[1,3],[2,3]]	                    3
3	[[1,3],[2,3],[3,1]]	                -1
3	[[1,2],[2,3]]	                    -1
4	[[1,3],[1,4],[2,3],[2,4],[4,3]]	     3

def solution(N, trust):
    return -1
'''

def solution(N, trust):
  for i in range(1, N + 1):
      if len(list(filter(lambda x: x[0] == i, trust))) > 0:
          continue
      if len(list(filter(lambda x: x[1] == i, trust))) == N - 1:
          return i
  return -1
print(solution(2, [[1,2]])) # 2
print(solution(3, [[1,3],[2,3]])) #3
print(solution(3, [[1,3],[2,3],[3,1]])) #-1
print(solution(3, [[1,2],[2,3]])) #-1
print(solution(4, [[1,3],[1,4],[2,3],[2,4],[4,3]])) #3