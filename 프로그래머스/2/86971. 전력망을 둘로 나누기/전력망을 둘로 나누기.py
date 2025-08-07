# # 모든 연결되어 있는것을 잘라보고 차이 구함
# # dfs로 각각 개수 세어서 차이 계산

# from collections import defaultdict

# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]

# cnt = 0

# def dfs(node, visited, graph):
#     visited[node] = True
#     count = 1
#     for next_node in graph[node]:
#         if not visited[next_node]:
#             count += dfs(next_node, visited, graph)
    
#     return count
        
        

# def solution(n, wires):
#     visited = [False for _ in range(n + 1)]
#     answer = n
    
#     for i in range(len(wires)):
#         graph = [[] for _ in range(n + 1)]
        
#         # 간선 자르기
#         temp_wires = wires[:i] + wires[i+1:]
#         print(temp_wires)
        
#         for a, b in temp_wires:
#             graph[a].append(b)
#             graph[b].append(a)
#         visited = [False] * (n + 1)    
        
#         first = dfs(1, visited, graph)
#         second = n - first
        
#         diff = abs(first - second)
#         answer = min(answer, diff)
    
#     return answer

from collections import deque

def bfs(node, visited, graph):
    visited[node] = True
    count = 1
    queue = deque([node])
    
    while queue:
        now = queue.popleft()
        
        for neighbor in graph[now]:
            if not visited[neighbor]:
                visited[neighbor] = True
                count += 1
                queue.append(neighbor)
        
    return count
    
def solution(n, wires):
    answer = n
    
    for i in range(len(wires)):
        temp_wires = wires[:i] + wires[i+1:]
        
        graph = [[] for _ in range(n + 1)]
        
        for a, b in temp_wires:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * (n + 1)
        
        first = bfs(1, visited, graph)
        second = n - first
        
        diff = abs(first - second)
        answer = min(diff, answer)
    return answer