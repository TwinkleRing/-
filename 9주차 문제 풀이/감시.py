import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())

array = []
cctvs = []

mins = 1e9

for x in range(n) :
    temp = list(map(int,input().split()))
    for y in range(m) :
        if 1 <= temp[y] <= 5 :
            cctvs.append([x, y, temp[y]])
    
    array.append(deepcopy(temp))

# dirs
# 0 : 왼쪽
# 1 : 위쪽
# 2 : 오른쪽
# 3 : 아래쪽

def checking_map(array, dirs, x, y) :
    array = deepcopy(array)

    for looking in dirs :
        if looking == 0 : # 왼쪽, x 고정
            for dy in range(y,-1,-1) :
                if array[x][dy] == 6 :
                    break
                elif array[x][dy] != 0 :
                    continue
                else :
                    array[x][dy] = "#"

        if looking == 1 :
            for dx in range(x,-1,-1) :
                if array[dx][y] == 6 :
                    break
                elif array[dx][y] != 0 :
                    continue
                else :
                    array[dx][y] = "#"

        if looking == 2 :
            for dy in range(y, len(array[0])) :
                if array[x][dy] == 6 :
                    break
                elif array[x][dy] != 0 :
                    continue
                else :
                    array[x][dy] = "#"

        if looking == 3:
            for dx in range(x, len(array)) :
                if array[dx][y] == 6 :
                    break
                elif array[dx][y] != 0 :
                    continue
                else :
                    array[dx][y] = "#"

    return array


def detecting(array, cctvs, idx) :
    global mins

    if idx == len(cctvs) :
        cnt = 0
        for x in range(len(array)) :
            cnt += array[x].count(0)

        mins = min(mins, cnt)
        return

    cctv = cctvs[idx]
    x, y, kind = cctv

    if kind == 1 :
        for i in range(4) :
            next_array = checking_map(array, [i], x, y)
            detecting(next_array, cctvs, idx + 1)
    
    if kind == 2 :
        for i in [(0,2),(1,3)] :
            next_array = checking_map(array, i , x, y) 
            detecting(next_array, cctvs, idx + 1)

    if kind == 3 :
        for i in [(1,2),(2,3),(3,0),(0,1)] :
            next_array = checking_map(array, i , x, y) 
            detecting(next_array, cctvs, idx + 1)

    if kind == 4 :
        for i in [(0,1,2),[1,2,3],[2,3,0],[3,0,1]] :
            next_array = checking_map(array, i, x, y) 
            detecting(next_array, cctvs, idx + 1)
    
    if kind == 5 :
        next_array = checking_map(array, [0, 1, 2, 3], x, y) 
        detecting(next_array, cctvs, idx + 1)


detecting(array, cctvs, 0)
print(mins)
