import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    

def bfs(start):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    hacking_cnt = 1
    
    while queue:
        now = queue.popleft()
        
        for next_node in graph[now]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True
                hacking_cnt += 1
    
    return hacking_cnt
        
result = []

for i in range(1, n + 1):
    result.append((bfs(i), i))
    
max_hacking = max(result)[0]

answer = [num for cnt, num in result if cnt == max_hacking]

answer.sort()
print(" ".join(map(str, answer)))
