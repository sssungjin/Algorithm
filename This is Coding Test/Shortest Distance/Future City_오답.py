import heapq
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for i in range(n + 1)]
distance_1toK = [INF] * (n + 1)
distance_KtoX = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    # a 번 노드에서 b번 노드로 가는 비용은 1
    graph[a].append((b, 1))

x, k = map(int, input().split())


def dijkstra(start, dist):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        dis, now = heapq.heappop(q)
        if dist[now] < dis:
            continue
        for i in graph[now]: 
            cost = dis + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

ans = 0    
dijkstra(1, distance_1toK)
dijkstra(k, distance_KtoX)
for i in range(1, n + 1):
    if distance_1toK[i] == INF:
        print("INFINITY")
    else:
        print(distance_1toK[i])

for i in range(1, n + 1):
    if distance_KtoX[i] == INF:
        print("INFINITY")
    else:
        print(distance_KtoX[i])


if distance_1toK[k] != INF:
    ans += distance_1toK[k]
    if distance_KtoX[x] != INF:
        ans += distance_KtoX[x]
        print(ans)
    else: print(-1)
else: print(-1)
