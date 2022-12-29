def solution(N, K, L, apples, moves):
    arr = [[0] * N for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        arr[x - 1][y - 1] = 1

    # 오른, 아래, 왼, 위, 명령에 따라 좌회전 또는 우회전을 하기 때문에 mod로 구현하고자 key값을 0~3으로 구성함
    delta = {0:(0, 1), 2:(0, -1), 1:(1, 0), 3:(-1, 0)}
    # 처음 시작 방향이 오른쪽
    direction = 0
    time = 0
    change = {}
    for _ in range(L):
        t, action = input().split()
        change[int(t)] = action
    x, y = 0, 0
    snake = deque([(0,0)])
    # delta에 따라 뱀의 머리를 이동시키고 사과가 있다면 그대로 진행
    # 사과가 없다면 꼬리를 제거한다.
    while True:
        time +=1
        dx, dy = delta[direction]
        x+=dx
        y+=dy
        # 시간에 따른 방향 전환
        if time in change.keys():
            if change[time] == 'L':
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4
        # 벽에 부딪친 경우
        if x < 0 or x >= N or y < 0 or y >= N:
            break
        # 자신의 몸통에 부딪친 경우
        if [x, y] in snake:
            break
        # 사과를 먹은 경우
        if arr[x][y] == 1:
            arr[x][y] = 0
            snake.append([x, y])
        # 사과가 없는 경우
        else:
            snake.append([x,y])
            # 꼬리 제거
            snake.popleft()

    return time

N = 6
K = 3
L = 3
apples = [(3, 4), (2, 5), (5, 3)]
moves = [(3, 'D'), (15, 'L'), (17, 'D')]
print(solution(N, K, L, apples, moves))

N = 10
K = 4
L = 4
apples = [(1, 2), (1, 3), (1, 4), (1, 5)]
moves = [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]
print(solution(N, K, L, apples, moves))

N = 10
K = 5
L = 4
apples = [(1, 5), (1, 3), (1, 2), (1, 6), (1, 7)]
moves = [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]
print(solution(N, K, L, apples, moves))