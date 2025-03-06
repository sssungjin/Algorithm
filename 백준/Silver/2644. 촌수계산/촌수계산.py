from collections import deque

n = int(input())
x, y = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(start, target):
    visited = [-1] * (n + 1)
    queue = deque([start])
    visited[start] = 0
    
    while queue:
        current = queue.popleft()
        if current == target:
            return visited[current]

        for next_node in graph[current]:
            if visited[next_node] == -1:
                visited[next_node] = visited[current] + 1
                queue.append(next_node)
                
    return -1
                
result = bfs(x, y)
print(result)
    
