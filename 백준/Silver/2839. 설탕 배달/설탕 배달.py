n = int(input())

INF = float('inf')

dp = [INF] * (n + 1)
dp[0] = 0

for i in range(3, n + 1):
    if i >= 3 and dp[i - 3] != INF:
        dp[i] = min(dp[i], dp[i - 3] + 1)
    if i >= 5 and dp[i - 5] != INF:
        dp[i] = min(dp[i], dp[i - 5] + 1)
        
    
print(dp[n] if dp[n] != INF else -1)