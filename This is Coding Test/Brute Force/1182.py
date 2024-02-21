from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(1, n+1):
    for combi in combinations(arr, i):
        if sum(combi) == s:
            ans += 1

print(ans)