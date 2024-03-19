def dfs(start):
    if len(arr) == m:
        print(' '.join(map(str, arr)))

    for i in range(start, n + 1):
        if visited[i]:
            continue
        visited[i] = True
        arr.append(i)
        dfs(i + 1)
        arr.pop()
        visited[i] = False

n, m = map(int, input().split())
arr = []
visited = [False] * (n + 1)

dfs(1)