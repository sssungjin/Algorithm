n = int(input())
arr = [list(input()) for _ in range(n)]

colors = ['C', 'P', 'Z', 'Y']

def check_max_candy(graph):
    max_count = 1
    
    for i in range(n):
        cnt = 1
        for j in range(n - 1):
            if graph[i][j] == graph[i][j+1]:
                cnt += 1
                max_count = max(max_count, cnt)
            else:
                cnt = 1

    for i in range(n):
        cnt = 1
        for j in range(n - 1):
            if graph[j][i] == graph[j+1][i]:
                cnt += 1
                max_count = max(max_count, cnt)
            else:
                cnt = 1
                
    return max_count

max_candy = 1

max_candy = max(max_candy, check_max_candy(arr))

for i in range(n):
    for j in range(n):
        # 오른쪽과 교환
        if j + 1 < n and arr[i][j] != arr[i][j+1]:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            max_candy = max(max_candy, check_max_candy(arr))
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        
        # 아래쪽과 교환
        if i + 1 < n and arr[i][j] != arr[i+1][j]:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            max_candy = max(max_candy, check_max_candy(arr))
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

print(max_candy)