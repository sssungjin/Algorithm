from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(start, target):
    visited = [False] * (n + 1)
    queue = deque([(start, 0)])
    visited[start] = True
    
    while queue:
        current, step = queue.popleft()
        
        if current == target:
            return step
        
        for i in graph[current]:
            if visited[i] == False:
                visited[i] = True
                queue.append((i, step + 1))
    return 0
    
    

result = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i != j:
            result[i] += bfs(i, j)
            
min_bacon = float('inf')
min_user = -1

for i in range(1, n + 1):
    bacon_number = result[i]
    if bacon_number < min_bacon:
        min_bacon = bacon_number
        min_user = i
        
print(min_user)