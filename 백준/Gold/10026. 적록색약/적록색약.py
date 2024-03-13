# 색약 - R = G 로 취급
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
visited1 = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]
graph1 = []
graph2 = []
answer_1 = 0
answer_2 = 0

for _ in range(n):
    tmp = list(input())
    graph1.append(tmp)
    graph2.append(tmp)

def bfs1(a, b):
    queue = deque()
    queue.append((a, b))
    color = graph1[a][b]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n and visited1[nx][ny] == False and graph1[nx][ny] == color:
                queue.append((nx, ny))
                visited1[nx][ny] = True

for i in range(n):
    for j in range(n):
        if visited1[i][j] == False:
            bfs1(i, j)
            answer_1 += 1

for i in range(n):
    for j in range(n):
        if graph2[i][j] == 'R':
            graph2[i][j] = 'G'

def bfs2(a, b):
    queue = deque()
    queue.append((a, b))
    color = graph2[a][b]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n and visited2[nx][ny] == False and graph2[nx][ny] == color:
                queue.append((nx, ny))
                visited2[nx][ny] = True

for i in range(n):
    for j in range(n):
        if visited2[i][j] == False:
            bfs2(i, j)
            answer_2 += 1

print(answer_1, answer_2)