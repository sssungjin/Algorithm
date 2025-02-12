import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited = [False] * (n + 1)
    
# def bfs(v):
#     q = deque()
#     q.append(v)
#     visited[v] = True
    
#     while q:
#         v = q.popleft()
#         for i in range(1, n + 1):
#             if not visited[i] and graph[v][i] == 1:
#                 visited[i] = True
#                 q.append(i)

# cnt = 0

# for i in range(1, n + 1):
#     if not visited[i]:
#         bfs(i)
#         cnt += 1
        
# print(cnt)

cnt = 0

def dfs(v):
    visited[v] = True
    
    for i in range(1, n + 1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        cnt += 1
            
print(cnt)