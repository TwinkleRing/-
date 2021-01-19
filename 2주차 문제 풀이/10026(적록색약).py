from collections import deque
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x, y) :
    q.append([x, y])
    chk[x][y] = 1
    while q :
        x, y = q.popleft()
        for k in range(4) :
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n :
                if painting[nx][ny] == painting[x][y] and chk[nx][ny] == 0 :
                    q.append([nx, ny])
                    chk[nx][ny] = 1


n = int(input())
painting = [list(map(str,input())) for _ in range(n)]
chk = [[0]*n for _ in range(n)]
q = deque()

cnt = 0
for i in range(n) :
    for j in range(n) :
        if chk[i][j] == 0 :
            bfs(i,j)
            cnt += 1
print(cnt, end = " ")

chk = [[0]*n for _ in range(n)]

for i in range(n) :
    for j in range(n) :
        if painting[i][j] == "G" :
            painting[i][j] = "R"

cnt = 0
for i in range(n) :
    for j in range(n) :
        if chk[i][j] == 0 :
            bfs(i,j)
            cnt += 1

print(cnt)
