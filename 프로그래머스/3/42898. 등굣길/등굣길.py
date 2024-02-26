def solution(m, n, puddles):
    answer = 0
    # m은 x(열), n은 y(행)
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    puddles = [[j, i] for [i, j] in puddles]
    
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 1 and j == 1: continue
            # 웅덩이라면
            if [i, j] in puddles:
                dp[i][j] = 0
            # 오른쪽, 아래쪽으로 이동할 수 있는 경우의 수 합
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                        
    return dp[n][m] % 1000000007