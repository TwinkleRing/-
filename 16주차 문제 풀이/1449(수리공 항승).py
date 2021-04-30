from collections import deque
n, L = map(int, input().split())

location = list(map(int,input().split()))
location.sort()

q = deque(location)

start = 0
cnt = 0

while q :
    loc = q.popleft()
    if start < loc :
        start = loc + L - 1
        cnt += 1


print(cnt)