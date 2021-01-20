from collections import deque
import sys

dx = [1,0,-1,0]
dy = [0,1,0,-1]

m , n = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(n)]

q = deque()

# 익은 토마토를 모두 큐에 넣기.
for i in range(n) :
    for j in range(m) :
        if array[i][j] == 1 :
            q.append([i,j])


while q :
    x, y = q.popleft()
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m :
            if array[nx][ny] == 0 :
                array[nx][ny] = array[x][y] + 1
                q.append([nx,ny])

count = 0
for i in range(n) :
    # 익지 않은 토마토가 있는 경우
    if 0 in array[i] :
        print(-1)
        exit()
    else :
        count = max(count, max(array[i]))

print(count - 1)