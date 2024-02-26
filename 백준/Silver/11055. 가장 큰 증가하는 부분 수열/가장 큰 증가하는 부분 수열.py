n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
dp[0] = arr[0]

for i in range(1, n):
    for j in range(i):
        # 증가한다면
        if arr[j] < arr[i]: 
            dp[i] = max(dp[i], dp[j] + arr[i])
        else:
            dp[i] = max(dp[i], arr[i])
# dp 1 101 3 53 113 
# ar 1 100 2 50 60 3 5 6 7 8
print(max(dp))