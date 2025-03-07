import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 입력 처리
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

paint_cnt = 0

def bfs(r, c):
    queue = deque([(r, c)])
    visited[r][c] = True
    paint_width = 1
    
    while queue:
        now_r, now_c = queue.popleft()
        
        for i in range(4):
            next_r, next_c = dr[i] + now_r, dc[i] + now_c
            if (0 <= next_r < n and 0 <= next_c < m and 
                not visited[next_r][next_c] and graph[next_r][next_c] == 1):
                queue.append((next_r, next_c))
                visited[next_r][next_c] = True
                paint_width += 1
    
    return paint_width

result = []

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j]:
            result.append(bfs(i, j))
            paint_cnt += 1

print(paint_cnt)
print(max(result) if result else 0)