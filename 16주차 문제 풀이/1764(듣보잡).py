n, m = map(int,input().split())

arr_1 = set()
arr_2 = set()
arr = []

for _ in range(n) :
    arr_1.add(input())

for _ in range(m) :
    arr_2.add(input())

arr = sorted(list(arr_1 & arr_2))

print(len(arr))
for i in arr :
    print(i)