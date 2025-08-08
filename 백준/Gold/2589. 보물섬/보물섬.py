from collections import deque
import sys

input = sys.stdin.readline

r, c = map(int, input().split())
maps = [list(input().strip()) for _ in range(r)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(start_r, start_c):
    queue = deque()
    queue.append((start_r, start_c))
    
    visited = [[-1] * (c) for _ in range(r)]
    visited[start_r][start_c] = 0
    cnt = 0
    
    while queue:
        now_r, now_c = queue.popleft()
        
        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]
            
            if 0 <= next_r < r and 0 <= next_c < c and visited[next_r][next_c] == -1 and maps[next_r][next_c] == 'L':
                visited[next_r][next_c] = visited[now_r][now_c] + 1
                cnt = max(cnt, visited[next_r][next_c])
                queue.append((next_r, next_c))
    
    return cnt

result = 0
for i in range(r):
    for j in range(c):
        if maps[i][j] == 'L':
            result = max(result, bfs(i, j))
            
print(result)