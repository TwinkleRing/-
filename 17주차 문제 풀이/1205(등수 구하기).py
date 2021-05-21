import sys
input = sys.stdin.readline

n, new_point, p = map(int,input().split())
ranking = list(map(int,input().split()))
answer = 0

if n == 0 :
    print(1)
else :
    if n == p and ranking[-1] >= new_point :
        print(-1)
    else :
        res = n + 1
        for i in range(n) :
            if ranking[i] <= new_point :
                res = i + 1
                break
        print(res)
