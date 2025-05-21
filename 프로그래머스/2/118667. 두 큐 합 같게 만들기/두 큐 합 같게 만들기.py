from collections import deque

def solution(queue1, queue2):
    answer = 0
    dq1 = deque(queue1)
    dq2 = deque(queue2)
    
    sum1 = sum(dq1)
    sum2 = sum(dq2)
    total = sum1 + sum2
    
    if total % 2 != 0:
        return -1
    
    target = total // 2
    max_ops = len(queue1) * 3
    count = 0
    p1, p2 = 0, 0

    while count <= max_ops:
        if sum1 == target:
            return count
        elif sum1 > target:
            num = dq1.popleft()
            sum1 -= num
            dq2.append(num)
            sum2 += num
        else:
            num = dq2.popleft()
            sum2 -= num
            dq1.append(num)
            sum1 += num
        count += 1
        
    return -1