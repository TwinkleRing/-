# 다이나믹 프로그래밍
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
D = [0] * 10001

coin = []
for _ in range(n) :
    coin.append(int(input()))

D[0] = 1

for i in coin :
    for j in range(i, k + 1) :
        D[j] += D[j - i]

print(D[k])
