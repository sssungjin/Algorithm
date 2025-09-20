from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    # sources 값이 destination에 갈 수 있는지, 가는 비용 answer에 저장, 못가면 -1
    graph = [[] for _ in range(n + 1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
        
    distances = [-1] * (n + 1)
    
    queue = deque([destination])
    distances[destination] = 0


        
    while queue:
        now = queue.popleft()    

        for i in graph[now]:
            if distances[i] == -1:
                distances[i] = distances[now] + 1
                queue.append(i)
    
    for s in sources:
        answer.append(distances[s])
    
    return answer