def dfs(v):
    visited[v] = True
    next = num[v]
    if not visited[next]:
        dfs(next)

t = int(input())

for _ in range(t):
    n = int(input())
    num = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    cnt = 0

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    print(cnt)