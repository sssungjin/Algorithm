from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    
    visited = [[False] * M for _ in range(N)]
    queue = deque([(0, 0)])
    
    visited[0][0] = True
    
    melt_cheese = []
    
    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                
                # 0이면 탐색
                if graph[nr][nc] == 0:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                if graph[nr][nc] == 1:
                    visited[nr][nc] = True
                    melt_cheese.append((nr, nc))
                    
    return melt_cheese

def calculate_cheese(graph):
    cheese_cnt = 0
    for row in graph:
        cheese_cnt += sum(row)
    
    return cheese_cnt
    
    
answer = 0

while True:
    
    current_cheese = calculate_cheese(graph)
    
    if current_cheese == 0:
        break
    
    last_cheese = current_cheese

    melt_list = bfs()
    
    for a, b in melt_list:
        graph[a][b] = 0

    answer += 1

print(answer)
print(last_cheese)