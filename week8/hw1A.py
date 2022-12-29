'''
과제 1

패캠이는 아메바를 분열시키는 취미가 생겼다. 
패캠이는 아메바 하나하나가 모두 소중하기 때문에, 
새로 생겨난 아메바는 모두 새로운 이름을 지어주기로 하였다. 
이번에 분열하기로 한 아메바는 아래와 같은 특성을 가진다.
- 아메바가 분열하여 두 개체로 완전히 나뉘는 데에는 1분이 걸린다.
- 분열한 아메바 중 하나는 곧바로 분열을 시작하고, 
  다른 하나는 1분간 휴식 후 분열을 시작한다.
- 분열하면 기존의 개체는 사라지고 새로운 두 개체가 생긴 것으로 본다.
- 분열되는 도중에는 기존의 개체가 남아있고, 
  아직 새로운 개체가 생겨나지 않은 것으로 본다.
패캠이는 아메바 한 개체를 분열 시키기 시작한 후, 
N분 후까지 만들어진 모든 아메바 개체에 새로운 이름을 지어주기로 했다. 
패캠이가 준비해야 하는 아메바의 이름은 총 몇 개인가?

입출력 예
N	return
2	5
4	15

def solution(N):
    answer = 0
    return answer
'''

def solution(N):
    stack = []
    stack.append((0, True)) # (level, ready)
    count = 1
    while stack:
        level, ready = stack.pop()
        if level >= N:
            continue
        if ready:
            stack.append((level + 1, True))
            stack.append((level + 1, False))
            count += 2
        else:
            stack.append((level + 1, True))

    return count

print(solution(2))      # 5
print(solution(4))      # 15