n = int(input())
graph = []
visited = [False for _ in range(n)]
# graph는 i에서 j로 이어져 있는지 입력
for _ in range(n):
    graph.append(list(map(int, input().split())))

# i에서 j로 갈 수 있으면 1 없으면 0
def dfs(v):
    for i in range(n):
        if not visited[i] and graph[v][i] == 1:
            visited[i] = True
            dfs(i) 

for i in range(n):
    dfs(i)
    for j in range(n):
        if visited[j]:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
    visited = [False for _ in range(n)]