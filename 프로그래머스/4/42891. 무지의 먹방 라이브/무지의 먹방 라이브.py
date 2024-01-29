import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    # 시간이 적은 음식부터 뺄 수 있도록
    for i in range(len(food_times)):
        # 음식 먹는 시간, 순번 삽입
        heapq.heappush(q, (food_times[i], i + 1))
    length = len(q)
    # 이전 음식 먹는데 걸린 시간
    pre = 0
    
    while q:
        # 몇초가 지나야 이 음식을 먹을 수 있는지
        eat_time = (q[0][0] - pre) * length
        
        # 만약 k 이하라면 그 다음 음식에 대한 시간 구해주기 위해서
        if eat_time <= k:
            # 먹는데 걸린 시간 빼주고
            k -= eat_time
            # 다음 음식 먹는데 걸리는 시간 저장
            pre = heapq.heappop(q)[0]
            # 하나 먹었으니까 길이는 -1
            length -= 1
        # k 이상이라면 먹는 도중 지연이 걸릴 것이기 때문에 해당 음식의 인덱스 반환
        else:
            # 순번 순으로 정렬
            q.sort(key=lambda x: x[1])
            # 순번 반환
            return q[k % length][1]
    return answer