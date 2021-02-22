from collections import deque
import sys
input = sys.stdin.readline

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left(d) :
    if d == 0 :
        return 3
    elif d == 1 :
        return 0
    elif d == 2 :
        return 1
    elif d == 3 :
        return 2

def back(d) :
    if d == 0 :
        return 2
    elif d == 1 :
        return 3
    elif d == 2 :
        return 0
    elif d == 3 :
        return 1

def bfs(x, y, d) :
    global count
    q.append([x, y, d])
    array[x][y] = 2

    while q :
        x, y, d = q.popleft()
        temp_d = d # 현재 방향 저장.
        for i in range(4) :
            temp_d = turn_left(temp_d) # 왼쪽부터 탐색
            nx = x + dx[temp_d]
            ny = y + dy[temp_d]

            if 0 <= nx < n and 0 <= ny < m and array[nx][ny] == 0 : # 왼쪽 방향에 청소 가능!
                count += 1
                array[nx][ny] = 2
                q.append([nx, ny, temp_d])
                break 
            
            elif i == 3 : # 네 방향 모두 청소 완료 or 벽인 경우
                nx = x + dx[back(d)] # 방향 유지한 채 후진
                ny = y + dy[back(d)]
                q.append([nx, ny, d])

                if array[nx][ny] == 1 : # 후진도 못한다!
                    return count


n, m = map(int,input().split())
x, y, d = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(n)]
count = 1
q = deque()

answer = bfs(x, y, d)
print(answer)