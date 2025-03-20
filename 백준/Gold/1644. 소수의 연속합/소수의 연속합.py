import math
n = int(input())

a = [False, False] + [True] * (n - 1)
prime_num = []

for i in range(2, n + 1):
    if a[i]:
        prime_num.append(i)
        for j in range(i * 2, n + 1, i):
            a[j] = False


start, end, sum_prime, ans = 0, 0, 0, 0

while end < len(prime_num):
    sum_prime += prime_num[end]
    
    while sum_prime >= n and start <= end:
        if sum_prime == n:
            ans += 1
        sum_prime -= prime_num[start]
        start += 1
    
    end += 1

print(ans)
    