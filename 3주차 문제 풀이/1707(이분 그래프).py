from collections import deque

k = int(input())

def bfs(start) :
    chk[start] = 1
    q.append(start)
    while q :
        node = q.popleft()
        for i in graph[node] :
            if chk[i] == 0 :
                chk[i] = -chk[node]
                q.append(i)
            else :
                if chk[i] == chk[node] :
                    return False
    
    return True

for i in range(k) :
    v, e = map(int,input().split())
    q = deque()
    flag = True
    graph = [[] for _ in range(v + 1)]
    chk = [0 for _ in range(v + 1)]

    for _ in range(e) :
        x, y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)

    

    for i in range(1, v + 1) :
        if chk[i] == 0 :
            if not bfs(i) :
                flag = False
                break

    print("YES" if flag else "NO")
   
