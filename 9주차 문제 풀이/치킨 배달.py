# 치킨 배달 

from itertools import combinations as cb
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(n)]

chichen = []
home = []

for i in range(n) :
    for j in range(n) :
        if array[i][j] == 1 :
            home.append([i,j])
        elif array[i][j] == 2 :
            chichen.append([i,j])

answer = 1e9

candidates = list(cb(chichen, m))

def home_to_chicken(candidate) :
    result = 0
    for hx, hy in home :
        temp = 1e9
        for cx, cy in candidate :
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp

    return result


for i in candidates :
    answer = min(answer, home_to_chicken(i))

print(answer)


