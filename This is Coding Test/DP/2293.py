n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

# dp[k] = 합이 k가 되는 경우의 수
dp = [0] * (k + 1)
MIN = min(coins)
dp[0] = 1

# 동전을 사용하는 가지 수를 늘려가며 dp 리스트 업데이트
# 1, 2, 5 
# 1사용하는경우
# 1을 사용하는 경우에다가 2도 같이 사용해서 만들 수 있는 경우 +
for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = dp[i] + dp[i - coin]

print(dp[k])