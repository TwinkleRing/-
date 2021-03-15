from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    union = deque() # 연합
    q.append([x, y])
    check[x][y] = 1
    populate = 0 # 연합의 총 인구수
    union_cnt = 0 # 연합인 나라의 수


    while q: # 연합 구하기
        x, y = q.popleft()
        union.append([x, y])
        populate += array[x][y]
        union_cnt += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and check[nx][ny] == 0 :
                if L <= abs(array[x][y]-array[nx][ny]) <= R : # 연합이 가능하다!
                    check[nx][ny] = union_cnt
                    q.append([nx, ny])

    # 모든 연합을 구하고나서.
    while union :
        x, y = union.popleft()
        array[x][y] = populate // union_cnt # 인구 이동!

    if union_cnt == 1: # 연합 없다
        return 0

    return 1

n, L, R = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
time = 0

while True:
    q = deque()
    check = [[0] * n for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(n):
            if check[i][j] == 0 :
                cnt += bfs(i, j)
    
    if cnt == 0 : # 인구 이동 불가
        break 

    time += 1

print(time)
