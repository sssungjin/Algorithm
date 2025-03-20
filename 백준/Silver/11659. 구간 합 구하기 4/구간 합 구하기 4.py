n, m = map(int, input().split())
arr = list(map(int, input().split()))

interval = [tuple(map(int, input().split())) for _ in range(m)]
prefix_sum = [0] * (n + 1) 

for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
    
for i in range(m):
    start, end = interval[i][0], interval[i][1]
    print(prefix_sum[end] - prefix_sum[start - 1])
    