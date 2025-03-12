n = int(input())

INF = float('inf')

dp = [INF] * (n + 3)

dp[0] = 0
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, n + 1):
    tmp1, tmp2, tmp3 = INF, INF, INF
    if i % 3 == 0 and dp[i // 3] != INF:
        tmp3 = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0 and dp[i // 2] != INF:
        tmp2 = min(dp[i], dp[i // 2] + 1)
    if i >= 2:
        tmp1 = min(dp[i], dp[i - 1] + 1)
    dp[i] = min(tmp3, tmp2, tmp1)
        
print(dp[n])