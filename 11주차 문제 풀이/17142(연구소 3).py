import sys
from copy import deepcopy
from itertools import combinations as cb
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def check(arr, visited) :
    for i in range(n) :
        for j in range(n) :
            if arr[i][j] != 1 and visited[i][j] == 0 :
                return False
    
    return True # 다 퍼트렸다!

def bfs(start) :
    global answer
    array = deepcopy(maps)
    
    visited = [[0] * n for _ in range(n)]
    last_change = 0
    
    q = deque()
    q.extend(start)


    # 0이 2로 바뀌는 마지막 순간만을 확인하면 된다.
    # 비활성 바이러스가 활성화 되는 경우는 '빈 칸에 바이러스를 퍼뜨리는 경우가 아니기 때문에
    while q :
        x, y, cnt = q.popleft()
        visited[x][y] = 1

        for k in range(4) :
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n :
                
                if visited[nx][ny] == 0 and array[nx][ny] != 1 :
                    visited[nx][ny] = 1

                    if array[nx][ny] == 0 :
                        array[nx][ny] = 2
                        last_change = cnt + 1

                    q.append((nx, ny, cnt + 1))


    if check(array, visited) :
        answer = min(answer, last_change)        


#_____________________________________________________________

n, m = map(int,input().split())

maps = []
virus = []

for i in range(n) :
    tmp = list(map(int,input().split()))
    for j in range(n) :
        if tmp[j] == 2 :
            virus.append((i, j, 0))

    maps.append(tmp)

# 활성화 시킬 바이러스를 선택하는 경우의 수
candidates = list(cb(virus, m))
answer = 1e9

for candidate in candidates :
    bfs(candidate)

if answer == 1e9 :
    print(-1)
else :
    print(answer)
