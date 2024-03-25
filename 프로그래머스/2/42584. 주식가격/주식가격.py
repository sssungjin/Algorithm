from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        price = queue.popleft()
        sec = 0
        for i in queue:
            sec += 1
            if price > i:
                break
        answer.append(sec)
    
    return answer