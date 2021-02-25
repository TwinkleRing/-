import sys
from collections import deque
from copy import deepcopy
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs() :
    global answer
    maps = deepcopy(graph)

    for x in range(n) :
        for y in range(m) :
            if maps[x][y] == 2 : # 바이러스 찾아서 저장.
                q.append([x, y])

    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if maps[nx][ny] == 0 :
                    maps[nx][ny] = 2
                    q.append([nx, ny])

    cnt = 0
    for i in maps :
        cnt += i.count(0)
    answer = max(answer, cnt)



def select_wall(num) :
    if num == 3 : # 벽을 다 세웠으니 바이러스 퍼트리자
        bfs()
        return

    for x in range(n) :
        for y in range(m) :
            if graph[x][y] == 0 :
                graph[x][y] = 1
                select_wall(num + 1)
                graph[x][y] = 0

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
answer = 0
q = deque()

select_wall(0)
print(answer)