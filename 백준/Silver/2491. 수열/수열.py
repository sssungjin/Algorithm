import sys
input = sys.stdin.readline
N = int(input())
data = list(map(int, input().split()))
dp = [1] * N
dp2 = [1] * N

for i in range(N - 1):
    if data[i + 1] >= data[i]:
        dp[i + 1] += dp[i]

for i in range(N - 1):
    if data[i + 1] <= data[i]:
        dp2[i + 1] += dp2[i]

print(max(max(dp), max(dp2)))