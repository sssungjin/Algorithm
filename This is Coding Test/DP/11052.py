n = int(input())
card = list(map(int, input().split()))
info = []
# idx value
info.append((0, 0))

for i in range(1, n+1):
    info.append((i, card[i-1]))

dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], info[j][1] + dp[i - j])
print(dp[n])