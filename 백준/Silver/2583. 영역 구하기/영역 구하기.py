from collections import deque

m, n, k = map(int, input().split())

rectangle = [list(map(int, input().split())) for _ in range(k)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = [[0] * n for _ in range(m)]

for x1, y1, x2, y2 in rectangle:
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1
    
def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 1
    area_size = 1
    
        
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny))
                area_size += 1
    
    return area_size

areas = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            areas.append(bfs(i, j))
            

areas.sort()
print(len(areas))
print(*areas)
