n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = max(arr)
right = sum(arr)
ans = right

while left <= right:
    mid = (left + right) // 2
    
    sum = 0
    cnt = 1
    
    for i in range(n):
        if sum + arr[i] <= mid:
            sum += arr[i]
        else:
            cnt += 1
            sum = arr[i
                      ]    
    if cnt <= m:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
        
print(ans)             