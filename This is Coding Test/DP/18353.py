# 최장 증가 부분 수열

n = int(input())
soldier = list(map(int, input().split()))

cnt = 0
dp = [1] * n
for i in range(1, n):
    for j in range(0, i):
    # 내림차순이 맞으면
        if soldier[j] > soldier[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))