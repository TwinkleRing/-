n, L, R = map(int,input().split())

# 두 나라의 인구 차이가 L명 이상, R명 이하라면 국경선 열기

array = [list(map(int,input().split())) for _ in range(n)] 
union = []

    # x축 비교
if L <= abs(array[0][0] - array[1][0]) <= R :
    union.append((0, 0))
    union.append((1, 0))

if L <= abs(array[0][1] - array[1][1]) <= R :
    union.append((0,1))
    union.append((1,1))

if L <= abs(array[0][0] - array[0][1]) <= R :
    union.append((0, 0))
    union.append((0,1))

if L <= abs(array[1][0] - array[1][1]) <= R :
    union.append((1,0))
    union.append((1,1))

# y축 비교
for x in range(n - 1) :
    for y in range(n - 1) :
        if L <= abs(array[x][y] - array[x][y + 1]) <= R :
            union.append((x, y))
            union.append((x, y + 1))

for y in range(n - 1) :
    for x in range(n - 1) :
        if L <= abs(array[x][y] - array[x + 1][y] <= R) :
            union.append((x, y))
            union.append((x + 1, y))
            




union = list(set(union))
sum = 0
for (x, y) in union :
    sum += array[x][y]


population = int(sum // len(union))

for (x, y) in union :
    array[x][y] = population


print(array)