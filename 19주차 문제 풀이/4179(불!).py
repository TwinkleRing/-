from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def fire() :
    qlen = len(fq)
    while qlen :
        x, y = fq.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and maze[nx][ny] == "." :
                maze[nx][ny] = "F"
                fq.append([nx,ny])
        qlen -= 1



def bfs(x,y) :
    q.append([x,y])
    check[x][y] = 1
    while q :
        qlen = len(q)
        while qlen :
            x, y = q.popleft()
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c : 
                    if check[nx][ny] == 0 and maze[nx][ny] == "." :
                        check[nx][ny] = check[x][y] + 1
                        q.append([nx,ny])
                elif nx < 0 or ny < 0 or nx >= r or ny >= c :
                    print(check[x][y])
                    return
            qlen -= 1
        fire()

    print("IMPOSSIBLE")
    return

    
            

r,c = map(int,input().split())

maze = [list(input()) for _ in range(r)]
check = [[0]*c for _ in range(r)]

q , fq = deque(), deque()

for i in range(r) :
    for j in range(c) :
        if maze[i][j] == "J" :
            x1,y1 = i,j
            maze[i][j] = "."
        elif maze[i][j] == "F" :
            fq.append([i,j])

fire()
bfs(x1,y1)

