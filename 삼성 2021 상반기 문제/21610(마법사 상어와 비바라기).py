# 마법사 상어와 비바라기

import sys
from collections import deque

input = sys.stdin.readline

dx = [0, -1, -1, -1 ,0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

cx = [-1, -1, 1, 1]
cy = [-1, 1, 1, -1]

n, m = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(n)]

command = []
for _ in range(m) :
    d, s = map(int,input().split())
    command.append((d - 1, s))


# 처음 비바라기 시전
cloud = deque()
cloud.append((n-1, 0))
cloud.append((n-1, 1))
cloud.append((n-2, 0))
cloud.append((n-2, 1))


# m번 이동 명령
for i in range(m) :
    
    d, s = command[i]
    check = [[0] * n for _ in range(n)]

    temp = deque()
    # 1. 구름 이동
    for _ in range(len(cloud)) :
        x, y = cloud.popleft()

        nx = (s * dx[d] + x) % n
        ny = (s * dy[d] + y) % n
        temp.append((nx, ny)) # 이동한 구름


    water_copy = deque()
    # 2. 
    for _ in range(len(temp)) :
        x, y = temp.popleft()
        check[x][y] = 1 # 구름이 사라진 위치
        array[x][y] += 1
        water_copy.append((x, y)) # 물 복사 버그


    # 4. 물복사 버그
    while water_copy :
        x, y = water_copy.popleft()
        cnt  = 0
        for k in range(4) :
            nx = x + cx[k]
            ny = y + cy[k]
            if 0 <= nx < n and 0 <= ny < n :
                if array[nx][ny] > 0 :
                    cnt += 1

        array[x][y] += cnt

    # 5. 
    for i in range(n) :
        for j in range(n) :
            if array[i][j] >= 2 and check[i][j] == 0 :
                array[i][j] -= 2
                cloud.append((i, j))
                
    
    

answer = 0  
for i in array :
    answer += sum(i)

print(answer)
    
   
