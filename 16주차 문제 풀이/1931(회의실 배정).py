import sys
input = sys.stdin.readline

n = int(input())
meeting = [list(map(int,input().split())) for _ in range(n)]


meeting.sort(key = lambda x : (x[1], x[0]))

cnt = 0
end_time = 0

for i, j in meeting : # 회의 시작 시간이 이전 회의가 끝나는 시간보다 늦어야한다.
    if i >= end_time :
        cnt += 1
        end_time = j
    
print(cnt)