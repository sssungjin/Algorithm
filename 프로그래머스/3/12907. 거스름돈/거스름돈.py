def solution(n, money):
    answer = 0
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    
    for coin in money:
        for j in range(coin, n + 1):
            dp[j] = dp[j] + dp[j - coin]
    return dp[n]