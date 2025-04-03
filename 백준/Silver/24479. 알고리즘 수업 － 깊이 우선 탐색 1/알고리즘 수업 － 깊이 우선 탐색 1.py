import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
        
visited = [0] * (N  + 1)
order = 1


def dfs(r):
    global order
    visited[r] = order
    order += 1
    
    for i in sorted(graph[r]):
        if visited[i] == 0:
            dfs(i)
            
dfs(R)

for i in range(1, N + 1):
    print(visited[i])