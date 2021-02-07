n = int(input())

array = [list(map(int,input().split())) for _ in range(n)]

for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            if array[i][k] == 1 and array[k][j] == 1 :
                array[i][j] = 1

    
for i in range(n) :
    for j in range(n) :
        print(array[i][j], end = " ")
    print()