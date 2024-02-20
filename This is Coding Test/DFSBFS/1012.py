from collections import deque

t = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
ans = []

def solution(n, m, graph):
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    num = 0
    # i는 행 j는 열
    for i in range(n):
        for j in range(m):
            # 방문하지 않았고 1이면(배추심어져있으면)
            if not visited[i][j] and graph[i][j] == 1:
                # 큐에 추가
                q.append((i, j))
                while q:
                    y, x = q.pop() # i행(y) j열(x)
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and graph[ny][nx] == 1:
                            visited[ny][nx] = True
                            q.append((ny, nx))
                num += 1
    ans.append(num)

for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for j in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    solution(n, m, graph)

for i in ans:
    print(i)