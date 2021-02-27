n = int(input()) # 수의 개수
array = list(map(int,input().split())) # 숫자 배열
add, sub, mul, div = map(int,input().split())

min_value = 1e9
max_value = -1e9

def dfs(i, now) :
    global min_value, max_value, add, sub, mul, div 
    if i == n :
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else :
        if add > 0 :
            add -= 1
            dfs(i + 1, now + array[i])
            add += 1
        if sub > 0 :
            sub -= 1
            dfs(i + 1, now - array[i])
            sub += 1
        if mul > 0 :
            mul -= 1
            dfs(i + 1, now * array[i])
            mul += 1
        if div > 0 :
            div -= 1
            dfs(i + 1, int(now / array[i]))
            div += 1

dfs(1, array[0])

print(max_value)
print(min_value)
