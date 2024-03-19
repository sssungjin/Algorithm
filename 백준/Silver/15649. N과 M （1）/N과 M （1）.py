n, m = map(int, input().split())
arr = []
visited = [False] * (n+1)

def solution():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        arr.append(i)
        solution()
        arr.pop()
        visited[i] = False

solution()