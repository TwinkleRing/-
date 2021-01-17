from collections import deque
import sys

dx = [1,0,-1,0]
dy = [0,1,0,-1]


n , m = map(int,input().split())
maps = [list(map(int,input())) for _ in range(n)]
chk = [[0] * m for _ in range(n)]


q = deque([])
q.append([0 ,0])
chk[0][0] = 1

while q :
    x ,y = q.popleft()
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m :
            if maps[nx][ny] != 0 and chk[nx][ny] == 0 :
                maps[nx][ny] = maps[x][y] + 1
                chk[nx][ny] = 1
                q.append([nx,ny])

print(maps[n - 1][m - 1])
