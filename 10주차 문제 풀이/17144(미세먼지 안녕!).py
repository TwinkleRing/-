import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def air_move() :
    # up (반시계 방향 순환)
    up = now[0]

    # 1
    temp = arr[up][C - 1]
    for i in range(C - 1, 1, - 1):
        arr[up][i] = arr[up][i - 1]
    arr[up][1] = 0

    # 2 
    temp_1 = arr[0][C - 1]
    for i in range(up - 1):
        arr[i][C - 1] = arr[i + 1][C - 1]
    arr[up - 1][C - 1] = temp

    # 3 
    temp_2 = arr[0][0]
    for i in range(C - 2):
        arr[0][i] = arr[0][i + 1]
    arr[0][C - 2] = temp_1

    # 4 
    for i in range(up - 1, 1, -1):
        arr[i][0] = arr[i - 1][0]
    arr[1][0] = temp_2


    # down (시계 방향 순환)
    down = now[1]

    # 1
    temp = arr[down][C - 1]
    for i in range(C - 1, 1, -1):
        arr[down][i] = arr[down][i - 1]
    arr[down][1] = 0

    # 2 
    temp_1 = arr[R - 1][C - 1]
    for i in range(R - 1, down + 1, -1):
        arr[i][C - 1] = arr[i - 1][C - 1]
    arr[down + 1][C - 1] = temp

    # 3 
    temp_2 = arr[R - 1][0]
    for i in range(C - 2):
        arr[R - 1][i] = arr[R - 1][i + 1]
    arr[R - 1][C - 2] = temp_1

    # 4 
    for i in range(down + 1, R - 1):
        arr[i][0] = arr[i + 1][0]
    arr[R - 2][0] = temp_2



def spread() :
    new = [[0 for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):

            # 미세먼지가 5 이상이어야 유의미한 계산 가능 
            if arr[i][j] >= 5:

                # 주변에 나눠줄 양
                each = arr[i][j] // 5
                
                # 주변에 나눠준 횟수 카운팅 위함
                count = 0

                # 사방 탐색
                for k in range(4):
                    
                    ndr = i + dr[k]
                    ndc = j + dc[k]

                    # 범위 안에 들어오고, 공기청정기의 자리가 아닌 경우
                    if 0 <= ndr < R and 0 <= ndc < C and arr[ndr][ndc] != -1:
                        
                        # 카운트를 1 늘려주고
                        count += 1
                        
                        # 새 배열에 미세먼지를 받은만큼 더해줌
                        new[ndr][ndc] += each
                
                # 나눠준 애 업데이트 (나눠준만큼 빼기)
                arr[i][j] = arr[i][j] - (count * each)

    # 두 배열 값 합치기 
    for i in range(R):
        for j in range(C):
            arr[i][j] += new[i][j]

#_____________________________________________________________________

# 세로, 가로, 초(반복 횟수)
R, C, T = map(int, input().split())

# 인풋으로 들어오는 배열 채우기
arr = []
for _ in range(R):
    arr.append(list(map(int, input().split())))

# 공기청정기 위치 찾기
now = (0, 0)
for i in range(R):
    if arr[i][0] == -1 and arr[i + 1][0] == -1:
        now = (i, i + 1) 
        break

# T번 반복
for _ in range(T):
    # 확산
    spread()

    # 순환 시켜주기
    air_move()

# 남은 미세먼지 수 계산
result = 0
for i in arr :
    result += sum(i)

# 공기청정기 2칸을 각각  -1로 표현했으니 최종값에 2를 더해줌 
print(result + 2)
