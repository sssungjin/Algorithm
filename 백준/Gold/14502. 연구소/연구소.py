from collections import deque
import copy

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def bfs():
    queue = deque()
    tmp = copy.deepcopy(board)
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 2:
                queue.append((i, j))

    # 바이러스의 위치
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
        
            if (0 <= nx < n) and (0 <= ny < m):
                if tmp[nx][ny] == 0:
                    tmp[nx][ny] = 2
                    queue.append((nx, ny))

    global result
    count = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                count += 1

    result = max(result, count)


def wall(count):
    if count == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                wall(count + 1)
                board[i][j] = 0



result = 0
wall(0)

print(result)