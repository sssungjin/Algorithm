n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
sum_arr = 0
ans = 0

while end < n:
    sum_arr += arr[end]
    
    while sum_arr >= m and start <= end:
        if sum_arr == m:
            ans += 1
        sum_arr -= arr[start]
        start += 1
    
    end += 1

print(ans)