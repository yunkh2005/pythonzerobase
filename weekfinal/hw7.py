from collections import deque

def solution(C, B):
    time = 0
    queue = deque()
    queue.append((B, 0))
    visited = [{} for _ in range(200001)]

    while C <= 200000:
        C += time #시간만큼 더해짐
        if time in visited[C]:
            return time
            # 이렇게 해준다면 이 시간대에 방문하게 된 것이므로 코니와 브라운이 만나게 된 시점을 알 수 있음

        for i in range(0, len(queue)):
            current_position, current_time = queue.popleft()
            new_time = current_time + 1

            new_position = current_position - 1
            if 0 <= new_position <= 20000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if 0 <= new_position <= 20000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if 0 <= new_position <= 20000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))
        time += 1
    return -1

print(solution(11, 2))