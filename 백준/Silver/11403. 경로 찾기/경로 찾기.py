from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

result = [[0] * n for _ in range(n)]

def bfs(start, n, graph, result):
    visited = [False] * n
    queue = deque([start])
    # visited[start] = True를 여기서 하지 말고, 실제 경로가 생길 때 체크
    
    while queue:
        current = queue.popleft()
        for next_node in range(n):
            if graph[current][next_node] == 1 and not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True
                result[start][next_node] = 1  # start에서 next_node로 도달 가능
                
                # 간접 경로 반영: current를 통해 next_node로 갔으니, current의 결과를 복사
                for j in range(n):
                    if result[current][j] == 1:
                        result[start][j] = 1

for i in range(n):
    bfs(i, n, graph, result)
    
for i in result:
    print(*i)