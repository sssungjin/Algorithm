import heapq

INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    # x에서 y로 가는데 z 비용이 든다.
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # pop 한 것보다 더 작으면 그냥 그대로 둠
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

messages, max_dist = 0, 0

for i in range(1, n + 1):
    if distance[i] != INF:
        messages += 1
        max_dist = max(max_dist, distance[i])

print(messages - 1, max_dist)
