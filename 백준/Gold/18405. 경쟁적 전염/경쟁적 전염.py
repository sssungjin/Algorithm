from collections import deque

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

virus = []
queue = deque()

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus.append([graph[i][j], 0, i, j])
virus.sort()
for v in virus:
    queue.append(v)

def bfs():
    while queue:
        virus_num, s_now, row, column = queue.popleft()
        if s_now == s:
            break
        for i in range(4):
            nr = row + d[i][0]
            nc = column + d[i][1]

            if 0 <= nr < n and 0 <= nc < n and graph[nr][nc] == 0: 
                graph[nr][nc] = virus_num
                queue.append([virus_num, s_now + 1, nr, nc])
        # print(queue)

bfs()
print(graph[x - 1][y - 1])