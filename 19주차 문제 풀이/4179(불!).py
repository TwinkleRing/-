# 불!(4179)

from collections import deque
import sys

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def fire() :
    qlen = len(fq)
    for i in range(qlen) :
        x, y = fq.popleft()
        for k in range(4) :
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < r and 0 <= ny < c and maze[nx][ny] == "." :
                maze[nx][ny] = "F" 
                fq.append([nx, ny])


def move(x, y) :
    q.append((x, y))
    chk[x][y] = 1
    while q :
        qlen = len(q) 
        for i in range(qlen) :
            x, y = q.popleft()
            for k in range(4) :
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < r and 0 <= ny < c :
                    if chk[nx][ny] == 0 and maze[nx][ny] == "." :
                        chk[nx][ny] = chk[x][y] + 1
                        q.append((nx, ny))
                elif nx < 0 or ny < 0 or nx >= r or ny >= c :
                    print(chk[x][y])
                    return
            
        fire()
    print("IMPOSSIBLE")
    return



r, c = map(int,input().split())

maze = [list(input()) for _ in range(r)]
chk = [[0] * c for _ in range(r)]

q, fq = deque(), deque()


for i in range(r) :
    for j in range(c) :
        if maze[i][j] == "J" :
            sx, sy = i, j
            maze[i][j] = "."
        elif maze[i][j] == "F" :
            fq.append([i, j])

fire()
move(sx, sy)
