def dfs(start):
    if len(arr) == m:
        print(' '.join(map(str, arr)))

    for i in range(start, n + 1):
        arr.append(i)
        dfs(i + 1)
        arr.pop()

n, m = map(int, input().split())
arr = []

dfs(1)