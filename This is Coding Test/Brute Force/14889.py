from itertools import combinations, permutations
import sys
input = sys.stdin.readline

n = int(input())
ability = [list(map(int, input().split())) for _ in range(n)]
ans = 1e9

for r1 in combinations(list(range(n)), n//2):
    start, link = 0, 0
    r2 = list(set(list(range(n))) - set(r1))
    for r in combinations(r1, 2):
        start += ability[r[0]][r[1]]
        start += ability[r[1]][r[0]]
    for r in combinations(r2, 2):
        link += ability[r[0]][r[1]]
        link += ability[r[1]][r[0]]
    ans = min(ans, abs(start-link))
print(ans)