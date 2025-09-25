# 상어 이동
# 전체 물고기 이동
import copy

# 상어가 이동할때는 방향 기준으로 *1 *2 *3 만큼 이동 가능 (칸 범위 안에서)

# 종료 조건은 상어가 먹을 물고기 없을 때
# 상어 방향에 확인했을 때 물고기 없으면 종료

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

board = [[0] * 4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    fish = []
    for j in range(4):
        fish.append([data[2 * j], data[2 * j + 1] - 1])
    board[i] = fish

max_score = 0


def dfs(sx, sy, score, board):
    global max_score
    score += board[sx][sy][0]
    max_score = max(max_score, score)

    board[sx][sy][0] = 0

    for f in range(1, 17):
        f_x, f_y = -1, -1
        for x in range(4):
            for y in range(4):
                if board[x][y][0] == f:
                    # 물고기 위치
                    f_x, f_y = x, y
                    break
        if f_x == -1 and f_y == -1:
            continue
        # 물고기 방향
        f_d = board[f_x][f_y][1]

        for i in range(8):
            nd = (f_d + i) % 8
            nx = f_x + dx[nd]
            ny = f_y + dy[nd]

            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                continue
            board[f_x][f_y][1] = nd
            board[f_x][f_y], board[nx][ny] = board[nx][ny], board[f_x][f_y]
            break

    s_d = board[sx][sy][1]
    for i in range(1, 4):
        nx = sx + dx[s_d] * i
        ny = sy + dy[s_d] * i

        if (0 <= nx < 4 and 0 <= ny < 4) and board[nx][ny][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(board))

dfs(0, 0, 0, board)
print(max_score)


