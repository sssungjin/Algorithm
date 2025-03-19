n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins = coins[::-1] 

ans = 0

for coin in coins:
    if coin <= k:
        ans += k // coin
        k = k % coin
    
    if k == 0:
        break
    
print(ans)
        