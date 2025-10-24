from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    # r, c, dist
    queue = deque([(0, 0, 1)])
    visited[0][0] = True
    
    # 0은 벽, 1은 길
    # 목적지는 [n-1][m-1]
    flag = False
    while queue:
        r, c, dist = queue.popleft()
        
        if r == (n - 1) and c == (m - 1):
            answer = dist
            flag = True
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and maps[nr][nc] == 1:
                queue.append((nr, nc, dist + 1))
                visited[nr][nc] = True
                
    if flag:
        return answer
    else: return -1
