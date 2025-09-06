from collections import deque

def solve():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    def count_cheese():
        count = 0
        for r in range(N):
            for c in range(M):
                if board[r][c] == 1:
                    count += 1
        return count
    
    def bfs():
        visited = [[False] * M for _ in range(N)]
        queue = deque([(0, 0)])
        visited[0][0] = True
        board[0][0] = -1
        
        while queue:
            r, c = queue.popleft()
            
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                    if board[nr][nc] == 0:
                        board[nr][nc] = -1
                        visited[nr][nc] = True
                        queue.append((nr, nc))
    
    time = 0
    while True:
        if count_cheese() == 0:
            print(time)
            break
    
        time += 1
        
        bfs()
        
        melt_candidates = []
        for r in range(N):
            for c in range(M):
                if board[r][c] == 1:
                    air_contact = 0
                    for i in range(4):
                        nr, nc = r + dr[i],c + dc[i]
                        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == -1:
                            air_contact += 1
                    
                    if air_contact >= 2:
                        melt_candidates.append((r, c))
        
        for r, c in melt_candidates:
            board[r][c] = 0
            
        for  r in range(N):
            for c in range(M):
                if board[r][c] == -1:
                    board[r][c] = 0
    
solve()