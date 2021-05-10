### 삼성 SW 역량테스트 2020 기출문제
### 시뮬레이션 & 구현 

import sys
input = sys.stdin.readline

# 북, 남, 서, 동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m, k = map(int,input().split())

array = []
for i in range(n) :
    array.append(list(map(int,input().split())))

# 모든 상어의 현재 방향 정보
directions = list(map(int,input().split()))

# 각 위치마다 [특정 냄새의 상어 번호, 특정 냄새의 남은 시간]을 저장하는 2차원 리스트
smell = [[[0, 0]] * n for _ in range(n)]

# 각 상어의 회전 방향 우선순위 정보
priorities = [[] for _ in range(m)]
for i in range(m) :
    for j in range(4) :
        priorities[i].append(list(map(int,input().split())))

def update_smell() :
    for i in range(n) :
        for j in range(n) :
            if smell[i][j][1] > 0 :
                smell[i][j][1] -= 1

            # 상어가 존재하는 해당 위치의 냄새를 k로 설정
            if array[i][j] != 0 :
                smell[i][j] = [array[i][j], k]


# 모든 상어를 이동시키는 함수
def move() :
    new_array = [[0] * n for _ in range(n)]

    for x in range(n) :
        for y in range(n) :
            # 상어가 존재하는 경우
            if array[x][y] != 0 :
                direction = directions[array[x][y] - 1] # 현재 상어가 보고있는 방향

                found = False
                
                # 일단 냄새가 존재하지 않는 곳이 있는지 확인
                for index in range(4) :
                    # 현재 상어가 바라보는 방향에서의 우선순위
                    nx = x + dx[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    ny = y + dy[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    
                    if 0 <= nx < n and 0 <= ny < n :

                        if smell[nx][ny][1] == 0 : # 냄새가 존재하지 않는 곳
                            directions[array[x][y] - 1] = priorities[array[x][y] - 1][direction - 1][index]

                            # 상어 이동시키기
                            if new_array[nx][ny] == 0 :
                                new_array[nx][ny] = array[x][y]
                            else :
                                new_array[nx][ny] = min(new_array[nx][ny], array[x][y])

                            found = True
                            break


                if found :
                    continue

                # 주변에 모두 냄새가 남아 있다면, 자신의 냄새가 있는 곳으로 이동
                for index in range(4) :
                    nx = x + dx[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    ny = y + dy[priorities[array[x][y] - 1][direction - 1][index] - 1]

                    if 0 <= nx < n and 0 <= ny < n :

                        if smell[nx][ny][0] == array[x][y] :
                            directions[array[x][y] - 1] = priorities[array[x][y] - 1][direction - 1][index]
                            new_array[nx][ny] = array[x][y]
                            break


    return new_array


time = 0
while True :
    update_smell()
    new_array = move()
    array = new_array
    time += 1

    check = True
    for i in range(n) :
        for j in range(n) :
            if array[i][j] > 1 :
                check = False

    if check :
        break


    if time >= 1000 :
        print(-1)
        exit()

print(time)
