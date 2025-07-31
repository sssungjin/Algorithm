import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().strip().split())) for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c, visited):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True
    
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dr[d]
            ny = y + dc[d]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and arr[nx][ny] > 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

# 덩어리 수 세기
def count_ice():
    visited = [[False] * m for _ in range(n)]
    count = 0
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited)
                count += 1
    return count

# 주위 물 개수 세서 빙산 녹이기
def melt():
    melt_list = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                water = 0
                for d in range(4):
                    ni = i + dr[d]
                    nj = j + dc[d]
                    if 0 <= ni < n and 0 <= nj < m:
                        if arr[ni][nj] == 0:
                            water += 1 
                melt_list[i][j] = water
    
    for i in range(n):
        for j in range(m):
            arr[i][j] = max(0, arr[i][j] - melt_list[i][j])
            
year = 0

while True:
    cnt = count_ice()
    if cnt == 0:
        print(0)
        break
    if cnt >= 2:
        print(year)
        break
    melt()
    year += 1