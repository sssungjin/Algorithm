from collections import deque

def solution(priorities, location):
    answer = 0
    arr = []
    for i in range(len(priorities)):
        arr.append((i, priorities[i]))
    queue = deque(arr)
    tmp = []
    
    while queue:
        loc, pri = queue.popleft()

        max_pri = 0
        for a, b in queue:
            max_pri = max(max_pri, b)
        
        
        if max_pri > pri:
            queue.append((loc, pri))
        else:
            tmp.append((loc, pri))
            
    for l, p in tmp:
        answer += 1
        if l == location:
            return answer
