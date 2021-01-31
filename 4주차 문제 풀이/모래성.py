import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

queue = deque()
h, w = map(int,input().split())
array = [list(input()) for _ in range(h)]
chk = [[0] * w for _ in range(h)]

def bfs() :
    time = 0
    
    while queue :
        len_q = len(queue)
        
        for i in range(len_q) :
            x, y = queue.popleft()
            for i in range(8) :
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx == h or ny < 0 or ny == w :
                    continue
                if chk[nx][ny] :
                    continue

                array[nx][ny] -= 1

                if array[nx][ny] == 0 :
                    queue.append((nx,ny))
                    chk[nx][ny] = 1

        time += 1

    return time            
            



for i in range(h) :
    for j in range(w) :
        if array[i][j] == "." :
            queue.append((i,j))
            chk[i][j] = 1
            array[i][j] = 0

        else :
            array[i][j] = int(array[i][j])             


print(bfs() - 1)
