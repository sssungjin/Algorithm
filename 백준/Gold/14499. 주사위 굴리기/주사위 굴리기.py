import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(N)]
command = list(map(int, input().strip().split()))

dice = [0] * 6

def roll(cmd):
    global dice
    top, bottom, east, west, north, south = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    if cmd == 1: # 동
        dice[0], dice[1], dice[2], dice[3] = west, east, top, bottom
    elif cmd == 2: # 서
        dice[0], dice[1], dice[2], dice[3] = east, west, bottom, top
    elif cmd == 3: # 북
        dice[0], dice[1], dice[4], dice[5] = south, north, top, bottom
    elif cmd == 4: # 남
        dice[0], dice[1], dice[4], dice[5] = north, south, bottom, top
    
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for cmd in command:
    nx, ny = x + dx[cmd], y + dy[cmd]
    
    if not(0 <= nx < N and 0 <= ny < M):
        continue
    
    roll(cmd)
    
    x, y = nx, ny
    
    if graph[x][y] == 0:
        graph[x][y] = dice[1]
    else:
        dice[1] = graph[x][y]
        graph[x][y] = 0
    
    print(dice[0])
            