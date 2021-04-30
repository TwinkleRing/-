import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int,input().split()))
array.sort()

result = 0
time = []

for i in array :
    result += i
    time.append(result)
    
print(sum(time))