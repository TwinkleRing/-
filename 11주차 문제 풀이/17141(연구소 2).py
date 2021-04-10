import sys
from copy import deepcopy
from itertools import combinations as cb
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def check(arr, visited):
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 1 and not visited[i][j]: # 빈 칸이 있다.
                return 0
    return 1

def bfs(start, maps) :
    global mins
    q = deque()
    array = deepcopy(maps)
    visited = [[0 for _ in range(n)] for _ in range(n)]

    for x, y in start :
        q.append((x, y ,0))
        visited[x][y] = 1

    if check(array, visited) : # m개 만큼의 바이러스가 있고, 나머지는 다 벽인 경우는 시작부터 다 바이러스가 퍼뜨려진 상황이다.
        mins = 0
        return

    while q :
        x, y, cnt = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n  :
                if array[nx][ny] != 1 and not visited[nx][ny] :
                    q.append((nx, ny, cnt + 1))
                    visited[nx][ny] = 1
            
    check_val = check(array, visited)
    if check_val :
        mins = min(mins, cnt) 
               
    return mins


mins = 1e9

n, m = map(int, input().split()) # 연구소의 크기, 놓을 수 있는 바이러스 개수

maps = []
virus = [] 

for i in range(n) :
    tmp = list(map(int,input().split()))
    for j in range(n) :
        if tmp[j] == 2 :  
            virus.append((i, j))
    
    maps.append(tmp)


# 활성화 시킬 바이러스를 선택하는 경우의 수
candidates = list(cb(virus, m))

for candidate in candidates :
    bfs(candidate, maps)    

if mins == 1e9 :
    print(-1)
else : 
    print(mins)
