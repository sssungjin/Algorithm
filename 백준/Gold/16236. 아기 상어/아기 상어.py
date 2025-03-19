from collections import deque

# 상하좌우 이동 방향
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(board, shark_x, shark_y, shark_size, N):
    visited = [[-1] * N for _ in range(N)]
    queue = deque([(shark_x, shark_y)])
    visited[shark_x][shark_y] = 0
    
    # 먹을 수 있는 물고기 리스트
    fish = []
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                # 상어 크기보다 작거나 같은 경우에만 이동 가능
                if board[nx][ny] <= shark_size:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                    # 먹을 수 있는 물고기라면 추가
                    if 0 < board[nx][ny] < shark_size:
                        fish.append((visited[nx][ny], nx, ny))
    
    return fish

def solve(N, board):
    # 아기 상어 초기 위치 찾기
    shark_x, shark_y = 0, 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                shark_x, shark_y = i, j
                board[i][j] = 0  # 상어 위치를 빈 칸으로
    
    shark_size = 2
    eaten = 0
    total_time = 0
    
    while True:
        # 먹을 수 있는 물고기 찾기
        fish = bfs(board, shark_x, shark_y, shark_size, N)
        if not fish:  # 더 이상 먹을 물고기가 없으면 종료
            return total_time
        
        # 거리, 행, 열 순으로 정렬해 우선순위 높은 물고기 선택
        fish.sort()  # (거리, x, y) 순으로 정렬됨
        dist, next_x, next_y = fish[0]
        
        # 상어 이동 및 물고기 먹기
        board[next_x][next_y] = 0
        shark_x, shark_y = next_x, next_y
        total_time += dist
        eaten += 1
        
        # 크기 증가 체크
        if eaten == shark_size:
            shark_size += 1
            eaten = 0
    
# 입력 처리
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(solve(N, board))