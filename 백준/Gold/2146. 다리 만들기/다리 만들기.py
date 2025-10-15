from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = [[False] * N for _ in range(N)]

def bfs_find_ground(r, c, num):
    
    queue = deque([(r, c)])
    visited[r][c] = True
    graph[r][c] = num
    
    while queue:
        now_r, now_c = queue.popleft()    
        
        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]
            
            if 0 <= next_r < N and 0 <= next_c < N and not visited[next_r][next_c] and graph[next_r][next_c] == 1:
                queue.append((next_r, next_c))
                visited[next_r][next_c] = True
                graph[next_r][next_c] = num
    
ground_num = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == 1:
            ground_num += 1
            bfs_find_ground(i, j, ground_num) 

q = deque()
distance = [[-1] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            q.append((i,j))
            distance[i][j] = 0

min_length = float('inf')

while q:
    now_r, now_c = q.popleft()
    
    for i in range(4):
        nr, nc = now_r + dr[i], now_c + dc[i]
        
        if 0 <= nr < N and 0 <= nc < N:
            if graph[nr][nc] != 0 and graph[nr][nc] != graph[now_r][now_c]:
                current_bridge = distance[now_r][now_c] + distance[nr][nc]
                min_length = min(min_length, current_bridge)
                
            elif graph[nr][nc] == 0:
                graph[nr][nc] = graph[now_r][now_c]
                distance[nr][nc] = distance[now_r][now_c] + 1
                q.append((nr, nc))
                
print(min_length)