# 드래곤 커브

# 동 북 서 남
dx = [0,-1,0,1]
dy = [1,0,-1,0]

max_int = 101
end_x ,end_y = 0, 0 # 끝점의 정보
dragon = [] # 이전 세대의 방향정보를 저장하는 스택
result = 0  # 출력할 개수

n = int(input()) # 드래곤 커브의 개수

a = [[0]*101 for _ in range(101)] # 격자

def make_generation() : # 스택을 조사하면서 드래곤 커브를 만드는 함수
    size = len(dragon) # 현재 스택의 크기 
    for i in range(size-1, -1, -1) : # 스택의 뒤에서 부터 꺼내면서
        dir = (dragon[i] + 1) % 4  # 다음 세대의 방향 정보를 생성한다.
        # 1은 2가 되고 2는 3, 3은 0 , 0은 1이 됩니다.

        # 다음 세대의 방향 정보를 바탕으로 다음 x,y를 찾고 이를 갱신한다.
        global end_x, end_y
        end_x = end_x + dx[dir]
        end_y = end_y + dy[dir]

        # 만들어진 드래곤 커브를 지도에 놓아준다.
        a[end_x][end_y] = True

        # 다음 세대를 위해 스택에 방향 정보를 넣어준다.
        dragon.append(dir)
 
# x,y,d,g = x,y는 드래곤 커브의 시작 점 , d는 시작 방향, g는 세대

for i in range(n) :
    y,x,d,g = map(int,input().split())

    # 기존 드래곤 커브의 스택을 비워준다.
    dragon.clear()

    # 시작점 표시
    a[x][y] = True
    
    # 0세대 미리 만들기
    end_x = x + dx[d]
    end_y = y + dy[d]
    
    # 0세대를 만든 이후 지도 에 표시한다.
    a[end_x][end_y] = True

    # 0세대의 방향 정보를 스택에 넣어둔다.
    dragon.append(d)

    # 반복문을 통해 0부터 차례차례 드래곤 커브르 만들면서 g세대 까지 만든다.
    for i in range(g) :
        # 드래곤 커브를 만들자.
        make_generation()


for i in range(max_int - 1) :
    for j in range(max_int - 1) :
        # 인접한 4칸의 정사각형이 모두 드래곤의 일부이면
        if a[i][j] and a[i+1][j] and a[i][j+1] and a[i+1][j+1] :
            # 갯수를 1 증가시킨다.
            result += 1

print(result)
