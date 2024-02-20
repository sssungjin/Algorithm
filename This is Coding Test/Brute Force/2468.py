import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# graph의 값이 height 이상이고 범위를 벗어나지 않는 경우 확인
def bfs(height):
    visited = [[False for _ in range(n)] for _ in range(n)]
    ans = 0
    q = deque()
    for i in range(n):
        for j in range(n):
            # 잠기지 않았고 방문하지 않았다면 큐에 추가 하고 
            if graph[i][j] >= height and not visited[i][j]:
                q.append((i, j))
                while q:
                    x, y = q.pop()
                    for k in range(4):
                        nx = dx[k] + x
                        ny = dy[k] + y
                        # 방문하지 않았고 잠기지 않았다면
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] >= height:
                            # 방문 처리
                            visited[nx][ny] = True
                            q.append((nx, ny))
                # while문 끝나면 한 안전영역 구한 것
                ans += 1
    return ans

def solution():
    max_height = -1e9
    for i in graph:
        max_height = max(max_height, max(i))

    safe_num = -1e9
    for i in range(max_height+1):
        safe_num = max(safe_num, bfs(i))
        #print(bfs(i))
    print(safe_num)

solution()


