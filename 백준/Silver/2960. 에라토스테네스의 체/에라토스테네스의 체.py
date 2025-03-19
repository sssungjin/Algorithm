n, k = map(int, input().split())

arr = [True] * (n + 1)
arr[0] = arr[1] = False

count = 0

for i in range(2, n + 1):
    if arr[i]:
        arr[i] = False
        count += 1
        if count == k:
            print(i)
            break
        
        for j in range(i * 2, n + 1, i):
            if arr[j]:
                arr[j] = False
                count += 1
                if count == k:
                    print(j)
                    break
        if count == k:
            break