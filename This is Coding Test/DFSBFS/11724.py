n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)
count = 0

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(i):
    # 방문 처리
    visited[i] = True    

    # graph와 연결된 노드들 순회
    for i in graph[i]:
        # 방문 안했다면
        if not visited[i]:
            # i 노드와 연결된거 확인
            dfs(i)
            
for i in range(1, n + 1):
    if not visited[i]:
        # i번 노드와 연결된게 없다면
        if not graph[i]:
            count += 1
            visited[i] = True
        else: # 연결된 그래프가 있다면
            dfs(i)
            count += 1

print(count)