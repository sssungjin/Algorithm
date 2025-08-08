import heapq

def solution(N, road, K):
    answer = 0
    
    graph = [[] for _ in range(N + 1)]
    
    for a, b, dist in road:
        graph[a].append((b, dist))
        graph[b].append((a, dist))

    # 1에서 다른 마을까지 걸리는 거리
    INF = float('inf')
    distance = [INF] * (N + 1)
    distance[1] = 0
    
    heap = [(0, 1)]

    while heap:
        dist, now = heapq.heappop(heap)
        
        # 저장되어있는 거리가 다음 마을까지의 거리보다 크다면 기존 거리 사용
        if distance[now] < dist:
            continue
        
        for to, cost in graph[now]:
            new_dist = dist + cost
            if new_dist < distance[to]:
                distance[to] = new_dist
                heapq.heappush(heap, (new_dist, to))
    
    for i in distance:
        if i <= K:
            answer += 1
    print(distance)
    return answer