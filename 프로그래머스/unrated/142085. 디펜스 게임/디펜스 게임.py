import heapq

def solution(n, k, enemy):    
    answer = 0
    sum = 0
    max_heap = []
    
    for i in enemy:
        heapq.heappush(max_heap, (-i, i))
        sum += i
        if sum > n:
            if k == 0:
                break
            sum -= heapq.heappop(max_heap)[1]
            k -= 1
        answer += 1
    return answer