# 백트래킹

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int,input().split()))
answer = 0

def solve(value) :
    global answer
    
    if len(array) == 2 :
        if answer <= value :
            answer = value
            return

    for i in range(1, len(array) - 1) :
        value += array[i - 1] * array[i + 1]
        tmp = array[i]
        del array[i]

        solve(value)

        array.insert(i, tmp)
        value -= array[i - 1] * array[i + 1]


solve(0)
print(answer)
