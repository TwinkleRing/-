from collections import deque
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y) :
    q.append([x,y])
    chk[x][y] = 1
    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if chk[nx][ny] == 0 and land[nx][ny] == 1 :
                    q.append([nx,ny])
                    chk[nx][ny] = 1


T = int(input())
for _ in range(T) :
    m,n,k = map(int,input().split())
    chk = [[0] * m for _ in range(n)]
    land = [[0] * m for _ in range(n)]

    for i in range(k) :
        a, b = map(int,input().split())
        land[b][a] = 1

    cnt = 0 
    result = []
    q = deque()

    for i in range(n) :
        for j in range(m) :
            if land[i][j] == 1 and chk[i][j] == 0:
                bfs(i,j)
                cnt += 1

    print(cnt)





