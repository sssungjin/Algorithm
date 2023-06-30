def solution(numbers, target):
    answer = 0
    nlist = []
    q = [(numbers[0], 0)]
    q.append((-1*numbers[0],0))
    while q:
        temp, idx = q.pop()
        idx += 1
        if idx < len(numbers):
            q.append((temp+numbers[idx],idx))
            q.append((temp-numbers[idx],idx))
        else:
            if temp == target:
                answer += 1
    return answer
        
            
            
        
    return answer