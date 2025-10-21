from collections import deque, Counter

def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n + 1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    # node, distance
    queue = deque([(1, 0)])
    
    node_dist = [-1] * (n + 1)
    node_dist[1] = 0
    
    while queue:
        node, dist = queue.popleft()
        
        for neighbor in graph[node]:
            if node_dist[neighbor] == -1:
                queue.append((neighbor, dist + 1))
                node_dist[neighbor] = dist + 1

    max_dist = 0
    
    for d in node_dist[1:]:
        if d != -1:
            max_dist = max(max_dist, d)
    answer = node_dist.count(max_dist)
    return answer