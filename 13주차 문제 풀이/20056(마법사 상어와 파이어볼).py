from collections import deque
import sys
from copy import deepcopy
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int,input().split())
array = [[deque() for _ in range(n)] for _ in range(n)]
q = deque()

for _ in range(m) :
    r, c, m, s, d = map(int,input().split())
    array[r-1][c-1].append((m, s ,d)) # 질량, 속도, 방향
    q.append([r-1, c-1])


for _ in range(k):
    temp = []
    qlen = len(q)
    for _ in range(qlen):
        x, y = q.popleft()
        for _ in range(len(array[x][y])):
            m, s, d = array[x][y].popleft()
            nx = (s * dx[d] + x) % n
            ny = (s * dy[d] + y) % n
            q.append([nx, ny])
            temp.append([nx, ny, m, s, d])

    for x, y, m, s, d in temp:
        array[x][y].append([m, s, d])
    
    # 2. 파이어볼 나누기
    for i in range(n) :
        for j in range(n) :

            if len(array[i][j]) > 1 :
                total_m = 0
                total_s = 0
                total_d = []

                odd, even, cnt = 0, 0, 0
                
                for fire in array[i][j] :
                    total_m += fire[0]
                    total_s += fire[1]
                    if fire[2] % 2 == 0 :
                        even += 1
                    else :
                        odd += 1
                    cnt += 1


                next_m = int(total_m // 5)
                next_s = total_s // len(array[i][j])
                
                array[i][j] = deque()

                if next_m == 0 :
                    continue

                    
                if even == cnt or odd == cnt :
                    for even in [0, 2, 4, 6] :
                        array[i][j].append([next_m, next_s, even])
                else :
                    for odd in [1, 3, 5, 7] :
                        array[i][j].append([next_m, next_s, odd])

                
answer = 0
for i in range(n) :
    for j in range(n) :
        if array[i][j] :
            for fire in array[i][j] :
                answer += fire[0]

print(answer)
                

