def solution(sx, sy, direction, gameMap, visited):
    x, y = sx, sy
    steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    ans = 0
    turn_time = 0

    while True:
        # 반시계 방향 90도 회전
        direction -= 1
        direction %= 4

        step = steps[direction]
        nx = x + step[0]
        ny = y + step[1]
        # 바라보는 방향이 안가봤고 육지라면 이동
        if visited[nx][ny] == 0 and gameMap[nx][ny] == 0:
            visited[nx][ny] = 1
            x, y = nx, ny
            ans += 1
            turn_time = 0
            continue
        else:
            turn_time += 1

        # 4방향 다 못간다면 일단 nx, ny를 뒤로 이동
        if turn_time == 4:
            nx = x - step[0]
            ny = y - step[1]
            # 육지여서 뒤로 갈 수 있으면 이동 확정
            if gameMap[nx][ny] == 0:
                x = nx
                y = ny
            else:
                break
            turn_time = 0
    print(ans)



def main():
    N, M = map(int, input().split())
    sx, sy, direction = map(int, input().split())
    gameMap, visited = [], []

    for _ in range(M):
        arr = list(map(int, input().split()))
        gameMap.append(arr)
    visited = [[0] * M for _ in range(N)]
    solution(sx, sy, direction, gameMap, visited)

if __name__ == "__main__":
    main()