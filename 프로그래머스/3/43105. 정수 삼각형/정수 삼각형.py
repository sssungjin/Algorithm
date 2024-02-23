def solution(triangle):
    answer = 0
    dp = [[0] * len(triangle) for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            # 맨 앞
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            # 맨 뒤
            if j == (len(triangle[i]) - 1):
                dp[i][j] = dp[i-1][j - 1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    answer = max(dp[-1])
    return answer