N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

# 0 가로 1 세로 2 대각선
dp = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]

#1행 2열 가로
dp[0][1][0] = 1

for c in range(2, N):
    if graph[0][c] == 0:
        dp[0][c][0] = dp[0][c - 1][0]

for r in range(1, N):
    for c in range(1, N):
        if graph[r][c] == 1:
            continue

        # r,c에다가 가로 방향으로 파이프 놓는 경우
        if c - 1 >= 0:
            dp[r][c][0] += dp[r][c-1][0] # 가로 -> 가로
            dp[r][c][0] += dp[r][c-1][2] # 대각선 -> 가로

        if r - 1 >= 0:
            dp[r][c][1] += dp[r - 1][c][1] # 세로 -> 세로
            dp[r][c][1] += dp[r - 1][c][2] # 대각선 -> 세로

        if r - 1 >= 0 and c - 1 >= 0:
            if graph[r-1][c] == 0 and graph[r][c-1] == 0:
                dp[r][c][2] += dp[r - 1][c - 1][0]
                dp[r][c][2] += dp[r - 1][c - 1][1]
                dp[r][c][2] += dp[r - 1][c - 1][2]

print(sum(dp[N-1][N-1]))





