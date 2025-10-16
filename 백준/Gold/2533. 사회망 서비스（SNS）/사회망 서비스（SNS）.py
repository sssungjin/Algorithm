# 얼리 아답터가 아닌 사람들은 자신의 모든 친구들이 얼리 아답터일 때만 이 아이디어를 받아들인다. 
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
dp = [[0, 0] for _ in range(N + 1)]
visited = [False] * (N + 1)

def dfs(current_node):
    visited[current_node] = True
    
    dp[current_node][1] = 1
    
    for neighbor in graph[current_node]:
        if not visited[neighbor]:
            dfs(neighbor)
            
            dp[current_node][0] += dp[neighbor][1]
            
            dp[current_node][1] += min(dp[neighbor][0], dp[neighbor][1])
            

dfs(1)

print(min(dp[1][0], dp[1][1]))