n = int(input())
array = list(map(int,input().split()))
b, c = map(int,input().split())

count = 0  # 필요한 부감독관의 수
for num in array :
    if num >= b : # 각 시험장의 응시자 수가 총감독관이 감시하는 수보다 많으면
        num -= b # 이제 부 감독관이 감시해야하는 인원

        if num % c == 0 :
            count += num // c
        else :
            count += num // c + 1 # 나머지가 발생하면 부감독관이 한 명 더 있어야한다.

print(count + n)