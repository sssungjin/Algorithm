def solution(board):
    answer = 0
    if not board:
        return 0
    
    n = len(board)
    m = len(board[0])
    dp = [[0] * m for _ in range(n)]
    max_len = 0
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i-1][j-1]) + 1
                max_len = max(max_len, dp[i][j])
    
    return max_len * max_len