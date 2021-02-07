# DFS & DP
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

#_____________________________________________________
def dfs(x, y):
    if dp[x][y]: 
        return dp[x][y]

    dp[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if s[x][y] < s[nx][ny]: # 대나무가 더 많다. 자리 이동 가능
                dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1) # 이동할 수 있는 곳보다 하루 더 살수있다!
    return dp[x][y]
#______________________________________________________________

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
result = 0

#______________________________________________________________

for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j)) # 최대 일수(day) 찾기
print(result)


# 각 칸에서 시작했을때의 최대 값을 구하고 상하좌우를 살펴서 더 큰 곳을 살피는데,
# 거기에 값이 있다면 본인 좌표에 그 값 + 1 을 넣어주면 된다.
# 네 방향이니까 네 방향 중 max 값 넣는다.

