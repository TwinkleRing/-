import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())
belt = deque(list(map(int,input().split())))
robot = deque([0] * n)

time = 0
while True :
    # 1. 
    belt.rotate(1)
    robot.rotate(1)
    robot[n - 1] = 0

    # 2. 
    if sum(robot) :
        for i in range(n - 2, -1, -1) :
            if robot[i] == 1 and robot[i + 1] == 0 and belt[i + 1] >= 1 :
                robot[i + 1] = 1
                robot[i] = 0
                belt[i + 1] -= 1

    robot[-1] = 0

    # 3. 
    if robot[0] == 0 and belt[0] >= 1 :
        robot[0] = 1
        belt[0] -= 1

    time += 1

    if belt.count(0) >= k :
        break

    
print(time)

