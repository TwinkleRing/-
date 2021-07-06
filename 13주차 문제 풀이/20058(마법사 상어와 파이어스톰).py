# 마법사 상어와 

import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 가장 큰 얼음 덩어리 찾기.
def bfs(x, y) :
    q = deque()
    q.append((x, y))
    chk[x][y] = 1

    cnt = 1

    while q :
        x, y = q.popleft()
        for k in range(4) :
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 2**n and 0 <= ny < 2**n :
                if chk[nx][ny] == 0 and array[nx][ny] != 0 :
                    q.append((nx, ny))

                    cnt += 1
                    chk[nx][ny] = 1

    return cnt



def check_around() :
    global array

    candidates = []

    for i in range(2**n) :
        for j in range(2**n) :

            cnt = 0
            for k in range(4) :
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or ny < 0 or nx >= 2**n or ny >= 2**n :
                    continue

                if array[nx][ny] != 0 :
                    cnt += 1

            if cnt < 3 and array[i][j] != 0 :
                candidates.append((i, j))

    for candidate in candidates : # 0이 되는 얼음들을 모아서 한꺼번에 1씩 감소시킨다.
        x, y = candidate
        if array[x][y] > 0 :
            array[x][y] -= 1



n, Q = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(2**n)]
level = list(map(int,input().split()))

# 파이어스톰 시전
for L in level :
    maps = [[0] * (2**n) for _ in range(2**n)]
    if L == 0 :
        check_around()
        continue

    for i in range(0, 2**n, 2**L) :
        for j in range(0, 2**n, 2**L) :
            # 시작점
            for s in range(0, 2**L) :
                for k in range(0, 2**L) :
                    maps[i + k][j + ((2**L) - 1) - s] = array[i + s][j + k]

    
    array = deepcopy(maps)
    check_around()



#_________________________________________________________________________________________

ans_area = 0
chk = [[0] * (2**n) for _ in range(2**n)]

for x in range(2**n) :
    for y in range(2**n) :
        if chk[x][y] == 0 and array[x][y] != 0 :
            ans_area = max(ans_area, bfs(x, y))
            
            

ans_sum = 0
for i in array :
    ans_sum += sum(i)

print(ans_sum)
print(ans_area)
