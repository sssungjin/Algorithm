import sys
from collections import defaultdict

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
sushi = sushi + sushi[:k-1]

left = 0
right = 0
max_cnt = 0

eat = defaultdict(int)
eat[c] = 1

for right in range(k):
    eat[sushi[right]] += 1
max_cnt = len(eat)

for right in range(k, len(sushi)):
    eat[sushi[right]] += 1
    
    eat[sushi[left]] -= 1
    if eat[sushi[left]] == 0:
        del eat[sushi[left]]
    left += 1
    
    max_cnt = max(max_cnt, len(eat))

print(max_cnt)