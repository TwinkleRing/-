### 구현, 시뮬레이션

import sys
input = sys.stdin.readline
from collections import Counter

r, c, k = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(3)]

time = 0
Flag = False
while time <= 100 :

    if r <= len(array) and c <= len(array[0]) :
        if array[r-1][c-1] == k :
            print(time)
            Flag = True
            break

    time += 1
    max_len = 0
    next_array = []

    # R 연산

    if len(array) >= len(array[0]) :
        for rows in array :
            next_row = []
            count_table = sorted(list(Counter(rows).items()), key = lambda x : (x[1], x[0]))
            for num, cnt in count_table :
                if num == 0 :
                    continue
                next_row.append(num)
                next_row.append(cnt)
            max_len = max(max_len, len(next_row))
            next_array.append(next_row)

        for rows in next_array :
            if len(rows) < max_len :
                for _ in range(max_len - len(rows)) :
                    rows.append(0)

        array = next_array
        continue

    
    # C 연산
    if len(array) < len(array[0]) :
        # 2차원 list transpose
        array = list(map(list, zip(*array)))

        for rows in array :
            next_row = []
            count_table = sorted(list(Counter(rows).items()), key = lambda x : (x[1], x[0]))
            for num, cnt in count_table :
                if num == 0 :
                    continue
                next_row.append(num)
                next_row.append(cnt)

            max_len = max(max_len, len(next_row))
            next_array.append(next_row)

        for rows in next_array :
            if len(rows) < max_len :
                for _ in range(max_len - len(rows)) :
                    rows.append(0)

        array = list(map(list, zip(*next_array)))
        continue



if not Flag :
    print(-1)
    
