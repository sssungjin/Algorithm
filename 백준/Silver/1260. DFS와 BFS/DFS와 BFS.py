from collections import deque

n, m, v = map(int, input().split())
graph = [[False] * (n+1) for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

# dfs는 재귀
def dfs(v):
    visited1[v] = True
    print(v, end=" ")

    for i in range(1, n + 1):
        # 방문하지 않았고 v와 i가 연결되어 있다면
        if not visited1[i] and graph[v][i] == 1:
            # 재귀호출
            dfs(i)
# bfs는 큐
def bfs(v):
    q = deque([v])
    visited2[v] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, n + 1):
            # 방문하지 않았고 v와 i가 연결되어 있다면 
            if not visited2[i] and graph[v][i] == 1:
                # i 푸시 및 방문 처리
                q.append(i)
                visited2[i] = True
dfs(v)
print()
bfs(v)