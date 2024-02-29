from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))

permu = list(permutations(arr, n))
answer = 0

for per in permu:
    total = 0
    for i in range(n - 1):
        total += abs(per[i] - per[i + 1])
    answer = max(total, answer)

print(answer)