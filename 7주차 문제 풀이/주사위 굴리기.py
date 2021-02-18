# 동 서 남 북 
# * 순서 꼭 지켜야함! *
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n, m, x, y, k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
direction = list(map(int,input().split()))
dice = [0 for _ in range(6)] # 위(천장) 북 동 서 남 아래(바닥)

for i in range(k) :
    dir = direction[i] - 1
    nx = x + dx[dir]
    ny = y + dy[dir]

    if nx >= n or nx < 0 or ny < 0 or ny >= m :
        continue 

    if dir == 0: # 동
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 1: # 서
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif dir == 2: # 남
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else : # 북
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    if board[nx][ny] == 0 :
        board[nx][ny] = dice[5]
    else :
        dice[5] = board[nx][ny]
        board[nx][ny] = 0

    x, y = nx, ny
    print(dice[0])

