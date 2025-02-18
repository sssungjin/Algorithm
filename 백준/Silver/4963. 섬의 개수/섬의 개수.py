from collections import deque
import sys
input = sys.stdin.readline

# 상 하 좌 우 대각선
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, 1, -1]

def bfs(graph, visited, r, c, weight, height):
    queue = deque([(r, c)])
    visited[r][c] = True
    
    while queue:
        row, col = queue.popleft()
        
        for i in range(8):
            nr = row + dr[i]
            nc = col + dc[i]
            
            if 0 <= nr < height and 0 <= nc < weight and not visited[nr][nc] and graph[nr][nc] == 1:
                visited[nr][nc] = True
                queue.append((nr, nc))
    

islands = []
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    visited = [[False] * w for _ in range(h)]
    
    graph = []    
    island_cnt = 0
    
    for i in range(h):
        graph.append(list(map(int, input().split())))
    
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j] == 1:
                island_cnt += 1
                bfs(graph, visited, i, j, w, h)
    islands.append(island_cnt)
    


    
for i in islands:
    print(i)