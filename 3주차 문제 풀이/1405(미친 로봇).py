import sys
input = sys.stdin.readline
dx = [1,-1,0,0]
dy = [0,0,1,-1]

N, e, w, s, n = map(int, input().split())
percent = [e/100, w/100, s/100, n/100]
Map = [[0 for _ in range(N*2 + 1)] for _ in range(N*2 + 1)]

def func(count, x, y):
    if count == N:
        return 1

    Map[x][y] = 1 # 방문 표시
    ret = 0
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]

        if Map[X][Y]: # 이미 방문하였다면 무시하고 진행
            continue

        ret += func(count + 1, X, Y) * percent[i] # Percent 곱해주기

    Map[x][y] = 0 #이렇게 해당 경우의 수를 다 조사한 뒤에는 방문한 지점을 지워줘야합니다.
    return ret

print(func(0, N, N))

# 단순하다는 것은 같은 곳을 또 다시 방문하지 않은 것.
# 4방향으로 탐색하고 만약 움직일 수 있는 횟수가 끝난다면 단순하다고 보면 됩니다.
# 그리고 그 모든 경우에 대한 Percent를 곱해주면 됩니다.
# 만약 방문하였다면 해당 경우는 고려하지 않고 진행합니다.

# 주의할 점은 어떤 지점을 방문하였다 하더라도 다른 경우에서는 그 지점을 방문하지 않았을 수도 있기 때문에
# 백트래킹으로 방문할 지점을 표시하고 다시 지워야한다.