from collections import deque
dx = [1,0,-1,0]
dy = [0,1,0,-1]

n = int(input())
maps = [list(map(int,input())) for _ in range(n)]
chk = [[0]*(n + 1) for _ in range(n + 1)]

def bfs(x,y) :
    cnt = 1
    q.append([x,y])
    chk[x][y] = 1
    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n :
                if chk[nx][ny] == 0 and maps[nx][ny] == maps[x][y] :
                    q.append([nx,ny])
                    chk[nx][ny] = chk[x][y] + 1
                    cnt += 1
                    
    return cnt

num = 0
result = []
q = deque([])
for i in range(n) :
    for j in range(n) :
        if maps[i][j] != 0 and chk[i][j] == 0 :
            result.append(bfs(i,j))
            num += 1


print(num)
result.sort()
for i in result :
    print(i, end = "\n")

