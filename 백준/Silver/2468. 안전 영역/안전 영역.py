from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

min_h = min(map(min, graph))
max_h = max(map(max, graph))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c, h, visited):
    q = deque([(r, c)])
    visited[r][c] = True
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc] and graph[nr][nc] > h:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    
max_safe_zone = 0

for h in range(min_h - 1, max_h + 1):
    visited = [[False] * n for _ in range(n)]
    safe_zone_count = 0
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > h:
                bfs(i, j, h, visited)
                safe_zone_count += 1
                
    max_safe_zone = max(max_safe_zone, safe_zone_count)
    
print(max_safe_zone)