dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = -1

def dfs(L, x, y, total):
    global answer
    if L == 4:
        answer = max(answer, total)
        return
    # 현재까지 합 + 가장 큰 값 * (남은 횟수) 가 answer 보다 작다면
    # 최댓값 나올 수 없으므로 확인할 필요가 없음
    elif total + max_value * (4 - L) <= answer:
        return
    else:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                # ㅗ ㅜ ㅏ ㅓ 모양 만들기 위해서 기존 블럭에서 다시 탐색
                if L == 2:
                    dfs(L+1, x, y, total + board[nx][ny])
                dfs(L + 1, nx, ny, total + board[nx][ny])
                visited[nx][ny] = False


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
max_value = max(map(max, board)) # map에서 가장 큰 값

for i in range(0, N):
    for j in range(0, M):
        visited[i][j] = True
        dfs(1, i, j, board[i][j])
        visited[i][j] = False

print(answer)