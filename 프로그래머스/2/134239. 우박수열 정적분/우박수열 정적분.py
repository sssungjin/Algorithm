def solution(k, ranges):
    answer = []
    woobak = [k]
    
    while k > 1:
        if k % 2 == 0:
            k = k // 2
        else:
            k = k * 3 + 1
        woobak.append(k)
    
    n = len(woobak) - 1
    width_arr = []
    
    for i in range(n):
        prev_height = woobak[i]
        next_height = woobak[i + 1]
        
        width = (prev_height + next_height) / 2
        
        width_arr.append(width)
    
    for a, b in ranges:
        start = a
        end = n + b
        tmp = 0
        if start > end:
            answer.append(-1)
            continue
        for i in range(start, end):
            tmp += width_arr[i]
        
        answer.append(tmp)
    
    return answer