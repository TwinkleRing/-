def dfs(idx, cnt) :
    global answer
    
    if cnt == k - 5 : # k개 다 배웠다!
        read_cnt = 0
        for word in words :
            for w in word :
                if not learn[ord(w) - ord('a')] : # 배우지 않은 것이 있다! 그러므로 못읽는다!
                    break

            else : 
                read_cnt += 1 # word를 읽을수 있다!

        answer = max(answer, read_cnt) if answer else read_cnt
        return

    for i in range(idx, 26) :
        if not learn[i] :
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False
    
#__________________________________________________________
n, k = map(int,input().split())
answer = 0

if k < 5 or k == 26 : # k가 5보다 작다면, 읽을 수 있는 단어는 없다!
    print(0 if k < 5 else n) # 그리고 k가 26이라면 모든 알파벳을 읽을 수 있다.
    exit(0)

words = [set(input()) for _ in range(n)]
learn = [False] * 26 

for char in ('a','n','t','i','c') :  # "anta" ~ "tica" 로 모든 단어가 이루어지므로, 
    learn[ord(char) - ord('a')] = True #  a, n, t, i, c 는 미리 체크!, ord()는 문자의 아스키 값을 반환한다. 

dfs(0, 0)
print(answer)