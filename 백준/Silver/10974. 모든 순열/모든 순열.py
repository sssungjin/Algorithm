n = int(input())
tmp = []

def dfs():
    if len(tmp) == n:
        print(*tmp)
        return
    for i in range(1, n+1):
        if i not in tmp:
            tmp.append(i)
            dfs()
            tmp.pop()
dfs()