from collections import deque

t = int(input())

dr = [-1, 1, 0, 0]
dc = [0 ,0, -1, 1]
ans = []

def bfs(graph, n, m):
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    num = 0
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 1:
                q.append((i, j))
                # 붙어 있는 배추
                while q:
                    r, c = q.popleft()
                    for k in range(4):
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and graph[nr][nc] == 1:
                            visited[nr][nc] = True
                            q.append((nr, nc))
                num += 1
    ans.append(num)
    
for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for j in range(k):
        x, y = map(int, input().split())        
        graph[y][x] = 1
    bfs(graph, n, m)
    

for i in ans:
    print(i)