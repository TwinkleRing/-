T = int(input())

for _ in range(T) :
    n = int(input())
    people = [list(map(int,input().split())) for _ in range(n)]
    people = sorted(people, key = lambda x : x[0]) # 서류 순서를 기준으로 오름차순 정렬

    
    tmp = people[0][1] 
    answer = 1 

    for i in range(1, n) :
        if people[i][1] < tmp : # 나(people[i][1])의 면접 순위가 더 높다!(순위는 낮아야 높은 것)
            tmp = people[i][1]
            answer += 1


    print(answer)

