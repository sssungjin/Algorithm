from collections import deque

dr = [-2, -1, -2, -1, 2, 1, 2, 1]
dc = [-1, -2, 1, 2, -1, -2, 1, 2]

def bfs(now_r, now_c, dest_r, dest_c, length):
    visited = [[False] * length for _ in range(length)]
    queue = deque([(now_r, now_c, 0)])
    visited[now_r][now_c] = True
    
    
    while queue:
        row, col, move_cnt = queue.popleft()
        
        if row == dest_r and col == dest_c:
            return move_cnt
        for i in range(8):
            nr = row + dr[i]
            nc = col + dc[i]
            
            if 0 <= nr < length and 0 <= nc < length and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc, move_cnt + 1))

t = int(input())

ans = []
for i in range(t):
    length = int(input())
    now_r, now_c = map(int, input().split())
    dest_r, dest_c = map(int, input().split())

    ans.append(bfs(now_r, now_c, dest_r, dest_c, length))
    
for i in ans:
    print(i)
