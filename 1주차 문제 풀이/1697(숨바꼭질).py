from collections import deque

n ,k = map(int,input().split())

time = [-1] * 100001
time[n] = 0

q = deque([n])
while q :
    n = q.popleft()
    if n == k :
        break

    for nx in [(n+1),(n-1),(n*2)] :
        if 0 <= nx < 100001 and time[nx] == -1 :
            time[nx] = time[n] + 1
            q.append(nx)


print(time[k])