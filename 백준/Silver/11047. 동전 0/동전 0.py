n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)
answer = 0

#while k != 0:
for coin in coins:
    # k보다 작거나 같으면
    if coin <= k:
        answer += k // coin
        k %= coin
        if k == 0:
            break 
print(answer)