from collections import deque

N, L, R = map(int, input().split())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

map = [list(map(int, input().split())) for _ in range(N)]

def bfs(r, c, visited):
    queue = deque([(r, c)])
    union = [(r, c)]
    visited[r][c] = True
        
    while queue:
        now_r, now_c = queue.popleft()
        for i in range(4):
            next_r = now_r + dr[i]
            next_c = now_c + dc[i]
            
            if 0 <= next_r < N and 0 <= next_c < N and not visited[next_r][next_c]:
                if L <= abs(map[now_r][now_c] - map[next_r][next_c]) <= R:
                    visited[next_r][next_c] = True
                    queue.append((next_r, next_c))
                    union.append((next_r, next_c))
    
    return union

def simulation():
    days = 0
    
    while True:
        visited = [[False] * N for _ in range(N)]
        moved = False
        
        for r in range(N):
            for c in range(N):
                if not visited[r][c]:
                    union = bfs(r, c, visited)
                    
                    if len(union) > 1:
                         moved = True
                         total_population = sum(map[x][y] for x, y in union)
                         avg_population = total_population // len(union)
                         
                         for x, y in union:
                            map[x][y] = avg_population
        
        if not moved:
            break
        days += 1
    return days

print(simulation())