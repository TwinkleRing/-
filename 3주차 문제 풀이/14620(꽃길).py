from itertools import combinations as cb
from collections import deque
dx = [0, 0, 1, 0, -1]
dy = [0, 1, 0, -1, 0]

n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]
max_cost = 200 * n * n

def solve(flowers) :
    cost = 0
    area = []
    for flower in flowers :
        row = flower // n
        col = flower % n
        if 0 < row < n - 1 and 0 < col < n - 1 :
            for k in range(5) :
                next_row = row + dx[k]
                next_col = col + dy[k]

                area.append((next_row, next_col))
                cost += maps[next_row][next_col]

        else :
            return max_cost

    if len(set(area)) == 15 :
        return cost

    return max_cost

def flower_cost(n, maps) :
    min_cost = max_cost

    comb_list = list(cb(range(n * n), 3))

    for flowers in comb_list :
        min_cost = min(min_cost, solve(flowers))

    return min_cost

print(flower_cost(n, maps))