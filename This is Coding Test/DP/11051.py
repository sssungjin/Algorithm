n, k = map(int, input().split())

# 팩토리얼 계산 값을 저장
dp = [1] * (n + 1)

for i in range(2, n+1):
    dp[i] = dp[i-1] * (i)

if k == 0 or k == n:
    print(1)
elif k == 1:
    print(n % 10007)
else:
    print((dp[n] // (dp[k] * dp[n - k])) % 10007)