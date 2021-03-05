import sys
from collections import deque


#왼쪽 톱니바퀴 확인
def check_left(start, dirs): 
    if start < 1 or gears[start][2] == gears[start + 1][6]:
        return 

    if gears[start][2] != gears[start + 1][6]:
        check_left(start - 1, -dirs)
        gears[start].rotate(dirs)

#오른쪽 톱니바퀴 확인
def check_right(start, dirs): 
    if start > 4 or gears[start-1][2] == gears[start][6]:
        return

    if gears[start][6] != gears[start-1][2] :
        check_right(start + 1, -dirs)
        gears[start].rotate(dirs)


gears = {}
for i in range(1, 5) :
    gears[i] = deque(list(map(int, input())))

n = int(input())
for _ in range(n):
    num, dirs = map(int,input().split())
    
    # 기준 톱니바퀴가 주어졌을 때, 오른쪽 / 왼쪽이 회전이 가능한지를 각각 확인하고 회전시킨다.
    check_left(num - 1, -dirs)
    check_right(num + 1, -dirs)
    # 기준 톱니바퀴를 회전시킨다.
    gears[num].rotate(dirs)

res = 0
for i in range(4) :
    res += (2**i) * gears[i + 1][0] 
print(res)