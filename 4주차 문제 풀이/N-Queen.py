# cur번째 행에 말을 배치할 예정
def func(row) :
    global cnt
    if row == n : # 각 행마다 퀸을 하나씩 다 놓는데 성공했다.
        cnt += 1
        return

    for col in range(n) : # 각 행(row)마다 열을 이동하면서
        if ( isused1[col] or isused2[col + row] or isused3[row - col + n - 1] ) : # 하나라도 걸리면 퀸 못 놓는다.
            continue
        # 현재 (row, col) 에 퀸을 둘 수 있으면 isused 1, isused 2, isused 3을 True로 변경하고 func(row + 1) 을 호출한다.
        isused1[col] = isused2[col + row] = isused3[row - col + n - 1] = 1 # 퀸을 놓는다.
        
        func(row + 1) # 다음 행에 퀸을 놓기 위해 재귀 호출
        
        isused1[col] = isused2[row + col] = isused3[row - col + n - 1] = False


# 우리는 각 행에 퀸을 한개씩만 놓으니까 한 행에 퀸이 2개인지는 생각할 필요 없다
#  열과 대각선만 생각하자. (열은 y좌표가 같은지만 체크하면 된다.)
#  좌측 하단과 우측 상단을 잇는 대각선은 x + y 가 같으면 같은 대각선에 위치해있다.
#  좌측 상단과 우측 하단을 잇는 대각선은 x - y 가 같으면 같은 대각선상에 위치한 것이다.

# isused 변수를 사용하여 모든 퀸에 대해 대각선 혹은 열에서 만나는 것이 있는지 확인

# isused1 은 각 열에 퀸이 있는지 체크 , isused2는 좌측 하단과 우측 상단 대각선 , isused3는 좌측 상단과 우측 하단 대각선 체크


n = int(input())
cnt = 0

isused1 = [False] * n # 수직선 위 체크
isused2 = [False] * (2 * n-1) # 우상향 대각선 체크
isused3 = [False] * (2 * n-1) # 좌상향 대각선 체크

func(0) # 0번째 행부터 시작!
print(cnt)



# 참고 : https://blog.encrypted.gg/945?category=773649