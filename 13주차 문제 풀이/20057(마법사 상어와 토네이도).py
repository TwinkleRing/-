# 백준 20057

import sys
input = sys.stdin.readline

# 서 남 동 북
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


# 모래가 흩날리는 좌표
move_left = [   # 토네이도가 왼쪽으로 이동하는 경우의 위치와 비율
                (-1, 0, 0.07), (-2, 0, 0.02), 
                (1, 0, 0.07), (2, 0, 0.02),
                (-1, 1, 0.01), (1, 1, 0.01),
                (-1, -1, 0.1), (1, -1, 0.1),
                (0, -2, 0.05), (0, -1, 0)
             ]

move_right= [  
                (-1, 0, 0.07), (-2, 0, 0.02),
                (1, 0, 0.07), (2, 0, 0.02),
                (-1, -1, 0.01), (1, -1, 0.01),
                (-1, 1, 0.1), (1, 1, 0.1),
                (0, 2, 0.05), (0, 1, 0)
            ]

move_up =   [  
                (-1, -1, 0.1), (-1, 1, 0.1),
                (0, 1, 0.07), (0, -1, 0.07),
                (1, -1, 0.01), (1, 1, 0.01),
                (-2, 0, 0.05), (0, -2, 0.02),
                (0, 2, 0.02), (-1, 0, 0)
            ]

move_down = [  
                (-1, -1, 0.01), (-1, 1, 0.01),
                (0, -1, 0.07), (0, 1, 0.07),
                (0, -2, 0.02), (0, 2, 0.02),
                (1, -1, 0.1), (1, 1, 0.1),
                (2, 0, 0.05), (1, 0 ,0)
            ]



# 이동 후 모래 날리기
def tornado(t) :
    global out_sand
    remove_sand = 0

    if t == "l" :
        rate = move_left
    elif t == "r" :
        rate = move_right
    elif t == "d" :
        rate = move_down
    elif t == "u" :
        rate = move_up

    for x, y, r in rate :
        # 먼지가 날아가는 위치 구하기
        nx = sx + x
        ny = sy + y

        if r == 0 : # 알파 구역에 날린 먼지 구하기
            s = array[sx][sy] - remove_sand
        else : # 비율에 따라 날린 먼지 구하기
            s = int(array[sx][sy] * r)

        if 0 <= nx < n and 0 <= ny < n :
            array[nx][ny] += s
        else :
            out_sand += s
        

        remove_sand += s


# 원하는 방향으로 cnt만큼 반복하여 이동
def push_sand(cnt, idx, t) :
    global sx, sy
    for _ in range(cnt + 1) :
        sx += dx[idx]
        sy += dy[idx]

        # (0, 0) 지점에 도달하는 경우 종료
        if sx < 0 or sy < 0 :
            break

        tornado(t)
    

n = int(input())
array = [list(map(int,input().split())) for _ in range(n)]
out_sand = 0 # 격자 밖으로 나간 모래의 양


# 토네이도는 격자 정 가운데에서 시작.
sx = n // 2
sy = n // 2

# 나선 모양으로 회전시키기
for i in range(n) :
    if i % 2 == 0 : # 왼쪽 아래쪽 2번
        push_sand(i, 0, "l") # 서 
        push_sand(i, 1, 'd') # 남
    else : # 오른쪽 위쪽 2번
        push_sand(i, 2, "r") # 동
        push_sand(i, 3, "u") # 북

print(out_sand)
