# 청소년 상어

from copy import deepcopy
import sys
input = sys.stdin.readline

# 반시계 8방향
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

def food(array, now_x, now_y) : # 상어가 현재 위치에서 먹을 수 있는 후보들의 위치 반환
    positions = []
    direction = array[now_x][now_y][1]

    for i in range(4) :
        now_x += dx[direction]
        now_y += dy[direction]
        if 0 <= now_x < 4 and 0 <= now_y < 4 :
            if 1 <= array[now_x][now_y][0] <= 16 :
                positions.append((now_x, now_y))

    return positions


def find_fish(array, index) :
    for i in range(4) :
        for j in range(4) :
            if array[i][j][0] == index :
                return (i, j)
    
    return None

def move_fish(array, now_x, now_y) :
    flag = False
    position = []
    for i in range(1, 17) :
        position = find_fish(array, i)
        if position != None :
            x, y = position[0], position[1]
            dirs = array[x][y][1]
            for j in range(8) :
                nx = x + dx[dirs]
                ny = y + dy[dirs]
                if 0 <= nx < 4 and 0 <= ny < 4 :
                    if not(nx == now_x and ny == now_y)  :
                        # 자리 교체
                        array[x][y][1] = dirs
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                        break
                dirs = (dirs + 1) % 8
            



def dfs(array, x, y, total) :
    global answer
    array =  deepcopy(array)

    # 해당 위치 물고기 먹기
    number = array[x][y][0]
    array[x][y][0] = -1

    # 물고기 이동
    move_fish(array, x, y)

    # 상어가 이동할 수 있는 후보 확인
    result = food(array, x, y)

    answer = max(answer, total + number)
    for nx, ny in result :
        dfs(array, nx, ny, total + number)



temp = [list(map(int,input().split())) for _ in range(4)]
array = [[None] * 4 for _ in range(4)]


 # 배열을 다루기 쉽게 [번호, 방향] 형태로 바꾼다.
for i in range(4) :
    for j in range(4) :
        array[i][j] = [temp[i][j * 2], temp[i][j * 2 + 1] - 1] 


answer = 0
dfs(array, 0, 0, 0)
print(answer)
