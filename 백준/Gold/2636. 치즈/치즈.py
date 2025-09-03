from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
 
def bfs():
    # visited 는 시간마다 초기화
    visited = [[False] * M for _ in range(N)]
    queue = deque([(0, 0)])
    visited[0][0] = True
    melt_list = []
    
    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            next_r, next_c = r + dr[i], c + dc[i]
            
            if 0 <= next_r < N and 0 <= next_c < M and not visited[next_r][next_c]:
                # 공기를 만나면 탐색
                if graph[next_r][next_c] == 0:
                    visited[next_r][next_c] = True
                    queue.append((next_r, next_c))
                # 치즈를 만나면 녹을 치즈로 간주하고 melt_list에 추가
                elif graph[next_r][next_c] == 1:
                    visited[next_r][next_c] = True
                    melt_list.append((next_r, next_c))
                    
    return melt_list

def count_cheese():
    count = 0
    for row in graph:
        count += sum(row)
    return count

time = 0
last_cheese_count = 0

while True:
    current_cheese_count = count_cheese()
    
    if current_cheese_count == 0:
        break
    
    last_cheese_count = current_cheese_count
    
    melt_list = bfs()
    
    for r, c in melt_list:
        graph[r][c] = 0
        
    time += 1

print(time)
print(last_cheese_count)