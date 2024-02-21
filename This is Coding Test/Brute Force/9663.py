# 8가지 방향 이동값
def check(x):
    for i in range(x):
        # 같은 열 또는 대각선이라면 놓을 수 없음
        if row[i] == row[x] or abs(row[x] - row[i]) == x - i:
            return False
    return True

def queen(depth):
    global ans

    if depth == n:
        ans += 1
    else:
        for i in range(n):
            #depth번째 행에 퀸 놓기
            row[depth] = i
            # 놓은게 올바르다면 재귀호출해서 다음행의 올바른 퀸을 놓도록
            if check(depth):
                queen(depth+1)


n = int(input())

# row의 인덱스가 행, value는 열을 나타냄
row = [0] * n
ans = 0

queen(0)
print(ans)
