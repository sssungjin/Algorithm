n = int(input())
num = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
# graph 연결 처리
for i in range(num):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1


def dfs(v):
    # 방문 = 감염
    visited[v] = True
    
    for i in range(2, n+1):
        # 방문하지 않았고 연결되어 있다면
        if not visited[i] and graph[v][i] == 1:
            dfs(i)

dfs(1)
print(visited.count(True) - 1)
