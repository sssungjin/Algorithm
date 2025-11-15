from collections import deque

def solution(board):
    N = len(board)
    
    # 0:상, 1:하, 2:좌, 3:우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # cost[행][열][방향] = (행, 열)까지 '방향'으로 도착했을 때의 최소 비용
    cost = [[[float('inf')] * 4 for _ in range(N)] for _ in range(N)]
    
    queue = deque()

    if N > 1 and board[1][0] == 0:
        cost[1][0][1] = 100 # (1,0)에 '아래'방향으로 도착한 비용
        queue.append((1, 0, 100, 1)) # (행, 열, 비용, 도착방향)
    
    if N > 1 and board[0][1] == 0:
        cost[0][1][3] = 100 # (0,1)에 '오른쪽'방향으로 도착한 비용
        queue.append((0, 1, 100, 3)) # (행, 열, 비용, 도착방향)

    while queue:
        r, c, current_cost, prev_dir = queue.popleft()
        
        for next_dir in range(4):
            nr, nc = r + dr[next_dir], c + dc[next_dir]
            
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 0:
                
                if prev_dir == next_dir:
                    new_cost = current_cost + 100
                else:
                    new_cost = current_cost + 600
                
                if new_cost < cost[nr][nc][next_dir]:
                    cost[nr][nc][next_dir] = new_cost
                    queue.append((nr, nc, new_cost, next_dir))

    answer = min(cost[N-1][N-1])
    return answer