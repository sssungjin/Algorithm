import sys
sys.setrecursionlimit(10**6)
# x를 기준으로 y와 연결되어 있는지

        
def solution(n, computers):

    def dfs(x):
        visited[x] = True
        for i in range(n):
            if not visited[i] and computers[x][i] == 1:
                dfs(i)
                
    answer = 0
    visited = [False] * n
                
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer