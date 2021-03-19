from collections import deque
import heapq
import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = int(input())
ocean = []
for x in range(n) :
    temp = list(map(int,input().split()))
    for y in range(n) :
        if temp[y] == 9 : # 아기 상어의 위치
            start = (x, y, 0)
    ocean.append(temp)


def bfs(start, ocean, current_size) :
    q = deque()
    q.append(start)
    x, y, cnt = start
    ocean[x][y] = 0 # 시작 지점은 0 처리!

    min_dist = []
    visited = set() # 방문 체크

    while q :
        x, y, cnt = q.popleft()
        visited.add((x, y))
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and (nx ,ny) not in visited :
                visited.add((nx, ny))

                if ocean[nx][ny] == 0 or ocean[nx][ny] == current_size :
                    q.append((nx, ny, cnt + 1))
                    continue
            
                if ocean[nx][ny] > current_size :
                    continue
                else :
                    heapq.heappush(min_dist, (cnt + 1, nx, ny))


    if min_dist :
        return min_dist[0]
    else :
        return None


time = 0 # 정답
current_size = 2 # 상어의 현재 크기
already_eat = 0

while True :
    next_value = bfs(start, ocean, current_size)

    if next_value is None : # 더 이상 물고기가 없다
        break

    cnt, nx, ny = next_value
    time += cnt

    already_eat += 1

    if already_eat == current_size :
        current_size += 1
        already_eat = 0 

    
    start = (nx ,ny, 0)

print(time)
