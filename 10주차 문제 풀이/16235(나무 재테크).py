# 시뮬레이션 & 구현

import sys
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

n, m, k = map(int,input().split())

land = [[5] * n for _ in range(n)]
A = [list(map(int, input().split())) for _ in range(n)]

maps = [[[] for _ in range(n)] for _ in range(n)]


for _ in range(m) :
    x, y, age = map(int,input().split())
    maps[x-1][y-1].append(age)


for i in range(k) :

    # 봄 & 여름
    for i in range(n) :
        for j in range(n) :
            if maps[i][j] :
                maps[i][j].sort() # 나이가 어린 나무 순서로 양분 공급
                # print(maps[i][j])
                temp_tree, dead_tree = [], 0
                for age in maps[i][j] :
                    if age <= land[i][j] :
                        land[i][j] -= age
                        age += 1
                        temp_tree.append(age)
                    else :
                        dead_tree += int(age // 2) # 죽은 나무가 양분으로 변한다.
                
                land[i][j] += dead_tree
                maps[i][j] = []
                maps[i][j].extend(temp_tree)

    if not maps :
        print(0)
        sys.exit()

    # 가을에는 나무가 번식한다.
    for i in range(n) :
        for j in range(n) :

            if maps[i][j] :
                for age in maps[i][j] :
                    if age % 5 == 0 :
                        for k in range(8) :
                            nx = i + dx[k]
                            ny = j + dy[k]
                            if 0 <= nx < n and 0 <= ny < n :
                                maps[nx][ny].append(1)

    # 겨울에는 땅에 양분을 추가
    for i in range(n) :
        for j in range(n) :
            land[i][j] += A[i][j]


# 살아있는 나무의 개수 구하기.
answer = 0
for i in range(n) :
    for j in range(n) :
        answer += len(maps[i][j])
        


print(answer)
