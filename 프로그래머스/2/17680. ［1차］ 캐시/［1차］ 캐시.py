def solution(cacheSize, cities):
    answer = 0
    # 가장 오랫동안 참조되지 않은 도시 이름 교체
    # 소요 시간은 큐에 있으면 1 없으면 5
    # 
    
    # 만약 들어있다면 해당 요소 없애고 맨 앞으로 땡김 (+1)
    # arr.find -> idx 찾고, del arr[idx], arr.append(city)
    # 없다면
    # 현재 길이가 cache size보다 작다면 그냥 append (+5)
    # 꽉 차있다면 맨 뒤에꺼 pop하고 현재 도시 append (+5)
    
    if cacheSize == 0:
        return len(cities) * 5
    
    queue = []
    
    for c in cities:
        city = c.upper()
        if city in queue:
            idx = queue.index(city)
            del queue[idx]
            queue.append(city)
            answer += 1
        else:
            # 공간 여유가 있다면 
            if len(queue) < cacheSize:
                queue.append(city)
            elif len(queue) >= cacheSize:
                del queue[0]
                queue.append(city)
            answer += 5
            
    return answer