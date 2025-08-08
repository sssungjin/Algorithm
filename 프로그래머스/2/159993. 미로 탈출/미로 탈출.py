from collections import deque

def solution(maps):
    def bfs(start_r, start_c, target):
        visited = [[False] * len(maps[0]) for _ in range(len(maps))]
        queue = deque()
        queue.append((start_r, start_c, 0))
        visited[start_r][start_c] = True
        
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]        
        
        while queue:
            r, c, dist = queue.popleft()
            
            if maps[r][c] == target:
                return dist
            
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                
                if 0 <= nr < len(maps) and 0 <= nc < len(maps[0]) and not visited[nr][nc] and maps[nr][nc] != 'X':
                    visited[nr][nc] = True
                    queue.append((nr, nc, dist + 1))
        return -1

    
    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] == 'S':
                sr, sc = r, c
            elif maps[r][c] == 'L':
                lr, lc = r, c
            elif maps[r][c] == 'E':
                er, ec = r, c
    
    dist_to_lever = bfs(sr, sc, 'L')
    if dist_to_lever == -1:
        return -1
    
    dist_to_exit = bfs(lr, lc, 'E')
    if dist_to_exit == -1:
        return -1
    
    return dist_to_lever + dist_to_exit