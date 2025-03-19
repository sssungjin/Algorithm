n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x: (x[1], x[0]))
available_time = 0
ans = 0

for i in range(n):
    start, end = arr[i][0], arr[i][1]
    
    if available_time <= start:
        available_time = end
        ans += 1

print(ans)
