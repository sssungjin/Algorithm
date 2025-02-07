from collections import deque
    
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(row, col):
    q = deque()
    q.append((row, col))
    
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 1:
                q.append((nr, nc))
                graph[nr][nc] = graph[r][c] + 1
                
                
n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int , input())))
    
bfs(0, 0)
print(graph[n-1][m-1])