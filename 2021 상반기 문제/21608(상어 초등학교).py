import sys
from collections import defaultdict

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = int(input())
array = [[0] * n for _ in range(n)]
dict_friend = defaultdict(list)
result = 0 # 만족도

for _ in range(n**2) :
    student, *f = map(int,input().split())
    dict_friend[student] = f

    x, y = 0, 0
    max_like = -int(1e9)
    max_empty = -int(1e9)

    for i in range(n) :
        for j in range(n) :

            if array[i][j] == 0 : 
                now_like = 0
                now_empty = 0
                for k in range(4) :
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n :
                        if array[nx][ny] in dict_friend[student] :
                            now_like += 1

                        elif array[nx][ny] == 0 :
                            now_empty += 1
                    
                if max_like < now_like or (max_like == now_like and max_empty < now_empty) :
                    x, y = i, j
                    max_empty = now_empty
                    max_like = now_like

    array[x][y] = student

# 만족도 구하기
for i in range(n) :
    for j in range(n) :
        cnt = 0
        like = dict_friend[array[i][j]] 
        for k in range(4) :
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n :
                if array[nx][ny] in like :
                    cnt += 1


        if cnt != 0 :
            result += 10**(cnt - 1)

print(result)