from collections import deque

n,m,v = map(int,input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visit = [False] * (n + 1)

for _ in range(m) :
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1


def dfs(v) :
    visit[v] = True
    print(v , end =" ")
    for i in range(1, n+1) :
        if not visit[i] and graph[v][i] == 1 :
            dfs(i)

def bfs(v) :
    q = deque([v])
    visit[v] = False
    while q :
        v = q.popleft()
        print(v, end = " ")
        for i in range(1, n + 1) :
            if visit[i] and graph[v][i] == 1 :
                q.append(i)
                visit[i] = False


dfs(v)
print()
bfs(v)