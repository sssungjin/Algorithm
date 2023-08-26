dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def solution(board):
    answer = 0
    queue = []
    #시작(R) 인덱스
    rx, ry = 0, 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                rx, ry = i, j
                queue.append((rx, ry))
                
    visited = [[0]*len(board[0]) for _ in range(len(board))]
    visited[rx][ry] = 1
    
    while queue:
        x, y = queue.pop(0)
        if board[x][y] == 'G':
            return visited[x][y] - 1
        
        for i in range(4):
            nx, ny = x, y
            while True:
                nx, ny = nx + dx[i], ny + dy[i]
                #멈추는 조건: 칸 안의 D를 만나거나 보드 밖으로 나갔을 때
                if (0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 'D') or nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]):
                        nx -= dx[i] #보드 밖이나 D의 위치에 있으면 안되므로 한 칸 앞으로
                        ny -= dy[i]
                        break
        
            if not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    return -1