n = int(input())
k = int(input())

maps = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

# 사과의 위치 저장
for _ in range(k) :
    a, b = map(int,input().split())
    maps[a][b] = 1

# 방향 변환 정보
info = []
l = int(input())
for _ in range(l) :
    x, c = input().split()
    info.append((int(x), c))

# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c) :
    if c == "L" :
        direction = (direction - 1) % 4
    else :
        direction = (direction + 1) % 4

    return direction

x, y = 1, 1
direction = 0 # 동쪽
maps[x][y] = 2
time = 0
index = 0 # 방향 변환 인덱스
q = [(x, y)]

while True :
    nx = x + dx[direction]
    ny = y + dy[direction]
    if 1 <= nx <= n and 1 <= ny <= n and maps[nx][ny] != 2 :
        if maps[nx][ny] == 1 :
            maps[nx][ny] = 2
            q.append((nx, ny))

        if maps[nx][ny] == 0 :
            maps[nx][ny] = 2
            q.append((nx, ny))
            px, py = q.pop(0)
            maps[px][py] = 0

    else :
        time += 1
        break
    
    time += 1
    x, y = nx, ny
    
    if index < l and time == info[index][0] :
        direction = turn(direction, info[index][1])
        index += 1

print(time)



