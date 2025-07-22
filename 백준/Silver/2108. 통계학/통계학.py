import sys 
input = sys.stdin.readline
from collections import Counter

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
c = Counter(arr)

# 평균
print(round(sum(arr) / n))
# 중앙값
print(arr[n // 2])

# 최빈값
if n > 1:
    tmp = c.most_common(2)
    if tmp[0][1] == tmp[1][1]:
        print(tmp[1][0])
    else:
        print(tmp[0][0])
else:
    print(arr[0])

# 범위
print(max(arr) - min(arr))