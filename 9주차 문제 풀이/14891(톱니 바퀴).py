import sys
from collections import deque

s = []
for _ in range(4) :
    s.append(deque(list(input())))

k = int(input())
R = [list(map(int,input().split())) for _ in range(k)]

def check_right(num, dir) :
    if num > 3 :
        return 
    
    if s[num][6] != s[num-1][2] :
        check_right(num + 1, -dir)
        s[num].rotate(dir)


def check_left(num ,dir) :
    if num < 0 :
        return 

    if s[num][2] != s[num+1][6] :
        check_left(num - 1, -dir)
        s[num].rotate(dir)


for i in range(k) :
    num = R[i][0] - 1
    direction = R[i][1]

    check_right(num + 1, -direction)
    check_left(num - 1, -direction)

    s[num].rotate(direction)


answer = 0

if s[0][0] == "1" :
    answer += 1
if s[1][0] == '1' :
    answer += 2
if s[2][0] == '1' :
    answer += 4
if s[3][0] == '1' :
    answer += 8

print(answer)
