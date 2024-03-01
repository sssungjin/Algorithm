from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            # 토마토 위치 저장
            queue.append((i, j))
        
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                # 현재 값 +1을 저장하면 며칠 지난지 알 수 있음
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
bfs()
answer = 0

# graph의 최댓값 -1 하면 정답
for row in graph:
    for i in row:
        if i == 0:
            print(-1)
            exit()
    else:
        answer = max(answer, max(row))

print(answer - 1)