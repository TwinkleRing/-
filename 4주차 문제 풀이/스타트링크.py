import sys
from collections import deque

input = sys.stdin.readline
F,S,G,U,D = map(int,input().split())

distance = [0] * (F + 1)

def bfs(v) :
    q = deque()
    q.append(v)
    distance[v] = 1
    while q :
        now = q.popleft()
        if now == G :
            print(distance[now] - 1)
            return 
        if now + U <= F and distance[now + U] == 0 :
            q.append(now + U)
            distance[now + U] = distance[now] + 1
        if now - D > 0 and distance[now - D] == 0 :
            q.append(now - D)
            distance[now - D] = distance[now] + 1
        
    print("use the stairs")

bfs(S)


