n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0

# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

while True:
    if graph[r][c] != 2:
        graph[r][c] = 2
        ans += 1
    
    cnt = 0
    # 청소할 칸 탐색
    while cnt < 4:
        cnt += 1
        d = (d - 1) % 4
        nr, nc = r + dr[d], c + dc[d]
        
        # 벽이 아니고 빈칸이라면
        if not graph[nr][nc] == 1 and graph[nr][nc] == 0:
            r, c = nr, nc
            break
    # 청소할 칸 없으면 후진
    else:
        lr, lc = r - dr[d], c - dc[d]
        if graph[lr][lc] == 1:
            break
        r, c = lr, lc

print(ans)