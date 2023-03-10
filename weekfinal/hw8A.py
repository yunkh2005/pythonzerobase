'''
'Dummy' 라는 도스게임이 있다. 
이 게임에는 뱀이 나와서 기어다니는데, 
사과를 먹으면 뱀 길이가 늘어난다. 
뱀이 이리저리 기어다니다가 벽 또는 
자기자신의 몸과 부딪히면 게임이 끝난다.
게임은 NxN 정사각 보드위에서 진행되고, 
몇몇 칸에는 사과가 놓여져 있다. 
보드의 상하좌우 끝에 벽이 있다. 
게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 
뱀은 처음에 오른쪽을 향한다.
뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.
먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
만약 이동한 칸에 사과가 있다면, 
그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
만약 이동한 칸에 사과가 없다면, 
몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 
즉, 몸길이는 변하지 않는다.
사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

입력
보드의 크기 N (2 ≤ N ≤ 100)
사과의 개수 K (0 ≤ K ≤ 100)
뱀의 방향 변환 횟수 L (1 ≤ L ≤ 100)
사과의 위치가 담긴 리스트 apples
첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 
사과의 위치는 모두 다르며, 
맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.
뱀의 방향 변환 정보 moves
정수 X와 문자 C로 이루어져 있으며. 
게임 시작 시간으로부터 X초가 끝난 뒤에 
왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. 
X는 10,000 이하의 양의 정수이며, 
방향 전환 정보는 X가 증가하는 순으로 주어진다.

예시입력1
입력
N = 6
K = 3
L = 3
apples = [(3, 4), (2, 5), (5, 3)]
moves = [(3, 'D'), (15, 'L'), (17, 'D')]
출력: 9

예시입력2
입력
N = 10
K = 4
L = 4
apples = [(1, 2), (1, 3), (1, 4), (1, 5)]
moves = [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]
출력: 21

예시입력3
입력
N = 10
K = 5
L = 4
apples = [(1, 5), (1, 3), (1, 2), (1, 6), (1, 7)]
moves = [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]
출력: 13
'''

def solution(N, K, L, apples, moves):
    board=[[0]*(N+1) for i in range(N+1)]
    for x, y in apples:
        board[x][y] = 1
    oper = moves
    snake=[(1,1)]
    d = [(0,1),(1,0),(0,-1),(-1,0)]
    d_f=0
    score=0
    x,y=1,1
    while True:
        score+=1
        x+=d[d_f][0]
        y+=d[d_f][1]
        if 1<=x<=N and 1<=y<=N:
            snake.append((x, y))
            for i in snake[:-1]:
                if (x, y)==i:
                    return score
            if board[x][y]==0:
                snake.pop(0)
            if board[x][y]==1:
                board[x][y]=0
        else:
            return score
        if oper and score==int(oper[0][0]):
            if oper[0][1]=='D':
                d_f= (d_f+1) % 4
                oper.pop(0)
            elif oper[0][1]=='L':
                d_f = (d_f - 1) % 4
                oper.pop(0)


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