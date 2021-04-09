import sys
from copy import deepcopy
from itertools import combinations as cb
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split()) # 연구소의 크기, 놓을 수 있는 바이러스 개수

maps = []
virus = [] 

for x in range(n) :
    tmp = list(map(int,input().split()))
    for y in range(n) :
        if tmp[y] == 2 : # 비활성 바이러스가 있다! 
            virus.append((x, y, 0))
    
    maps.append(tmp)


def check(maps) :
    for x in range(n) :
        for y in range(n) :
            if maps[x][y] == 0 : # 빈칸이 하나라도 있다!
                return -1

    return 0


def bfs(start, maps) :
    visited = [[0 for _ in range(n)] for _ in range(n)]
    maps = deepcopy(maps)
    q = deque()

    q.extend(start)
    last_change = 0

    # 0이 2로 바뀌는 마지막 순간만을 확인하면 된다.
    # 비활성 바이러스가 활성화 되는 경우는 '빈 칸에 바이러스를 퍼뜨리는 경우가 아니기 때문에
    while q :
        x, y, cnt = q.popleft()
        visited[x][y] = 1
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n :
                if not visited[nx][ny] and maps[nx][ny] != 1 : # 벽이 아니고, 방문 한 곳도 아니면 퍼트린다.
                    visited[nx][ny] = 1

                    if maps[nx][ny] == 0 : # 빈칸이면 바이러스 퍼트린다.
                        maps[nx][ny] = 2
                        last_change = cnt + 1

                    q.append((nx, ny, cnt + 1))
    
    # 빈 칸이 있는지 확인.
    val = check(maps)
    if val == 0 :
        return last_change
    else :
        return -1


mins = 1e9

# 활성화 시킬 바이러스를 선택하는 경우의 수
candidates = list(cb(virus, m))

for v in candidates :
    result = bfs(v, maps)
    if mins > result and result != -1 :
        mins = result


if mins == 1e9 :
    print(-1)
else :
    print(mins)
