import math

def solution(n):
    answer = 0
    
    for i in range(2, n + 1):
        flag = 0
        for a in range(2, int(math.sqrt(i)) + 1):
            if i % a == 0:
                flag = 1
                break
        if flag == 0:
            answer += 1
        
    
    return answer