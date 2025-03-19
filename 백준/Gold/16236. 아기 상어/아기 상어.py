from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 이동 방향: 위, 왼쪽, 오른쪽, 아래 순으로 (문제 우선순위 반영)
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

# 상어 초기 설정
shark_size = 2
shark_eaten = 0

# 상어 초기 위치 찾기
def find_shark():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 9:
                arr[i][j] = 0  # 상어 위치 초기화
                return i, j
    return None, None

def bfs(shark_r, shark_c, shark_size):
    queue = deque([(shark_r, shark_c, 0)])  # (행, 열, 거리)
    visited = [[False] * n for _ in range(n)]
    visited[shark_r][shark_c] = True
    
    min_dist = float('inf')
    edible_fish = None
    
    while queue:
        r, c, dist = queue.popleft()
        
        # 현재 거리가 이미 최소 거리를 넘으면 더 탐색할 필요 없음
        if dist > min_dist:
            break
        
        # 먹을 수 있는 물고기 발견
        if 0 < arr[r][c] < shark_size:
            min_dist = dist
            if edible_fish is None or (r, c) < edible_fish[1:]:  # 위쪽, 왼쪽 우선
                edible_fish = (dist, r, c)
            continue
        
        # 다음 위치 탐색
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and arr[nr][nc] <= shark_size:
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1))
    
    return edible_fish

# 메인 로직
total_time = 0
shark_r, shark_c = find_shark()

while True:
    result = bfs(shark_r, shark_c, shark_size)
    if not result:
        break
    
    move_time, fish_r, fish_c = result
    total_time += move_time
    
    # 상어 이동 및 물고기 먹기
    arr[fish_r][fish_c] = 0
    shark_r, shark_c = fish_r, fish_c
    
    shark_eaten += 1
    if shark_eaten == shark_size:
        shark_size += 1
        shark_eaten = 0

print(total_time)