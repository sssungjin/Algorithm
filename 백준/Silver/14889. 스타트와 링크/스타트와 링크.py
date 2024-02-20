import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [False for _ in range(n)]
min_value = 1e9

def dfs(depth, idx):
    global min_value
    if depth == n//2:
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                # visit 돌면서 True 쌍을 찾아서 점수 더함
                if visit[i] and visit[j]:
                    power1 += graph[i][j]
                # False 쌍을 찾아서 더함
                elif not visit[i] and not visit[j]:
                    power2 += graph[i][j]
        min_value = min(min_value, abs(power1-power2))
        return
    for i in range(idx, n):
        if not visit[i]:
            visit[i] = True
            dfs(depth+1, i+1)
            visit[i] = False
dfs(0, 0)
print(min_value)