a = input()
b = input()

dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(len(a) + 1):
    for j in range(len(b) + 1):
        if i == 0:
            dp[i][j] = j
        elif j == 0:
            dp[i][j] = i
        else:
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

print(dp[len(a)][len(b)])
