from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0

def turn(alpha):
    global direction
    if alpha == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

def solution(N, board, dirDict):
    queue = deque()
    queue.append((0, 0))
    cnt = 0
    x, y = 0, 0
    board[x][y] = 1

    while True:
        cnt += 1
        x += dx[direction]
        y += dy[direction]

        if x < 0 or x >= N or y < 0 or y >= N:
            break
        
        # 사과일때
        if board[x][y] == 2:
            board[x][y] = 1
            queue.append((x, y))
            if cnt in dirDict:
                turn(dirDict[cnt])
        elif board[x][y] == 0:
            board[x][y] = 1
            queue.append((x, y))
            tx, ty = queue.popleft()
            board[tx][ty] = 0
            if cnt in dirDict:
                turn(dirDict[cnt])
        else:
            break

    print(cnt)


def main():
    N = int(input())
    K = int(input())
    board = [[0] * N for _ in range(N)]

    for _ in range(K):
        a, b = map(int, input().split())
        board[a-1][b-1] = 2
        
    L = int(input())
    dirDict = dict()
    queue = deque()
    queue.append((0, 0))
    for _ in range(L):
        a, b = input().split()
        dirDict[int(a)] = b
    
    solution(N, board, dirDict)


if __name__ == "__main__":
    main()