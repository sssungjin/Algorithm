n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 1
ans = 0

while right <= n and left <= right:
    sum_arr = arr[left:right]
    total = sum(sum_arr)
    
    if total == m:
        ans += 1
        right += 1
    elif total < m:
        right += 1
    else:
        left += 1
        
print(ans)