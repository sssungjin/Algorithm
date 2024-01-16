N, M = map(int, input().split())
arr = []

for i in range(N):
    arr.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or y <= -1 or x >= N or y >= M:
        return False
    
    if arr[x][y] == 0:
        arr[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)
