import sys
import heapq
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# Get input
n, m, fuel = map(int, input().split())

array = []
for i in range(n) :
    array.append(list(map(int,input().split())))
    for j in range(n) :
        if array[i][j] == 1 :
            array[i][j] = -1

x, y = map(int,input().split())
pos_taxi = [x - 1, y - 1]

client_info = dict()

for i in range(m):
    sx, sy, ex, ey = map(int, input().split())
    sx, sy, ex, ey = sx-1, sy-1, ex-1, ey-1

    # Marking client in Board
    array[sx][sy] = i + 1

    # Store client_info for 목적지를 쉽게 찾기 위하여
    client_info[(sx, sy)] = (ex, ey)


def find_client(pos_taxi, fuel):
    global array
    x, y = pos_taxi

    # 1. 택시와 승객의 위치가 같을 경우
    if array[x][y] > 0 :
        # 지도의 해당 위치의 승객 없애기
        array[x][y] = 0
        return (x, y, 0)

    q = deque()
    q.append((x ,y))

    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    client_pq = []
    dist = 0

    while q :
        # 거리보다 연료가 적으면 더 이상 갈 수 없음으로
        dist += 1
        if dist > fuel :
            return -1

        # 이런식으로 for문을 걸어주면 dist별로 client를 확인할 수 있음
        for _ in range(len(q)):
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < n :
                    if visited[nx][ny] == False and array[nx][ny] != -1:
                        q.append((nx, ny))
                        visited[nx][ny] = True

                        if array[nx][ny] :
                            heapq.heappush(client_pq, (nx, ny, dist))

        if client_pq :
            x, y, dist = heapq.heappop(client_pq)
            array[x][y] = 0
            return (x, y, dist)

    return -1


def move_to_dest(pos_taxi, dest, fuel):
    x, y = pos_taxi

    if pos_taxi == dest:
        return 0

    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    q = deque()
    q.append(pos_taxi)
    dist = 0
    while q:
        dist += 1
        if fuel < dist:
            return -1
        # print('fuel, dist', fuel, dist)
        for i in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n :
                    if visited[nx][ny] == False and array[nx][ny] != -1:
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        if (nx, ny) == dest:
                            return dist

    # 에초에 도달할 수 없는 경우
    return -1
                    

for i in range(m):
    next_client = find_client(pos_taxi, fuel)
    
    if next_client == -1: # 승객 없다!
        print(-1)
        exit()
    else:
        nx, ny, dist_client = next_client
        pos_taxi = (nx, ny)
        
    fuel -= dist_client # 승객을 태우러 갈때 소비한 연료
    # print(fuel)
    dest = client_info[pos_taxi] # 목적지 위치
    dist = move_to_dest(pos_taxi, dest, fuel)

    if dist == -1: # 목적지까지 갈 수 없다.
        print(-1)
        exit()
    else:
        pos_taxi = dest # 택시는 목적지 위치에서 다시 출발.

    fuel += dist
    
print(fuel)

