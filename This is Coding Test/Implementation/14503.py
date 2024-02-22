# from collections import deque

# def solution():
#     global ans, d
#     queue = deque()
#     # 시작 좌표
#     queue.append((r, c))
#     while queue:
#         flag = 0
#         # print("============")
#         # print(graph)
#         row, col = queue.pop()
#         # 현재 위치가 청소되지 않았을 경우 청소하고 +1


#         # 반시계 방향으로 확인할 때 현재 보고 있는 방향인 d부터 확인해야함
#         for _ in range(4):
#             nr = row + dr[(d+3) % 4]
#             nc = col + dc[(d+3) % 4]

#             # 범위 안에 있고 청소하지 않았다면
#             if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 0 and not graph[nr][nc] == 1:
#                 queue.append((nr, nc))
#                 d = (d + 3) % 4
#                 graph[row][col] = 2
#                 ans += 1
#                 flag = 1
#                 break 
#             d += 1
#         # for문이 break로 끝난게 아니라면 뒤로 후진
#         if flag == 0:
#             # 현재 방향 + 2를 4로 나눈 나머지를 현재 좌표에 더하면 후진
#             nr = row + dr[(d+2) % 4]
#             nc = col + dc[(d+2) % 4]
#             # 범위 안에 있고 벽이 아니라면
#             if graph[nr][nc] == 1:
#                 break
#             else:
#                 row, col = nr, nc
#         print("+============================")
#         for k in graph:
#             print(k)


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