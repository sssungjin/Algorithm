N = int(input())
a = list(map(int, input().split()))
k = int(input())

def merge(arr, left, mid, right):
    temp = []
    p1 = left
    p2 = mid + 1
    
    while p1 <= mid and p2 <= right:
        if arr[p1] <= arr[p2]:
            temp.append(arr[p1])
            p1 += 1
        else:
            temp.append(arr[p2])
            p2 += 1
        
    while p1 <= mid:
        temp.append(arr[p1])
        p1 += 1
    
    while p2 <= right: 
        temp.append(arr[p2])
        p2 += 1
    
    for i in range(len(temp)):
        arr[left + i] = temp[i]
        

chunk_size = 2

while chunk_size <= N // k:
    merge_unit_size = chunk_size // 2
    start = 0
    while start < N:
        left = start
        mid = start + merge_unit_size - 1
        right = min(start + chunk_size - 1, N - 1)

        if mid < right:
             merge(a, left, mid, right)

        start += chunk_size

    chunk_size *= 2

print(*a)