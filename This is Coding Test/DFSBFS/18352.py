from collections import deque

n, m, k, x = map(int, input().split())
# 그래프 n+1 크기로 만들어서 1부터 시작하도록
g = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])
while q:
    start = q.popleft()

    for nx in g[start]:
        # 방문 안했으면
        if distance[nx] == -1:
            distance[nx] = distance[start] + 1
            q.append(nx)
tf = False

for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        tf=True
if tf == False:
    print(-1)





