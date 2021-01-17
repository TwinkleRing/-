from itertools import combinations as cb

L , C = map(int,input().split())
array = list(input().split())
array.sort()

# 모음
vowels = ['a','e','i','o','u']

candidates = list(cb(array, L))

for candi in candidates :
    count = 0
    for letter in candi :
        if letter in vowels :
            # 모음은 최소 1개가 있어야한다.
            count += 1
    # 4글자 암호에서 모음은 최소 1개이고 자음은 최소 2개이다.
    if 1 <= count <= L-2 :
        print(''.join(candi))