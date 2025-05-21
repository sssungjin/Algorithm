def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    arr = []
    
    for i in range(0, len(score) - m + 1, m):
        arr.append(score[i:i+m])
        
    
    for i in arr:
        answer += min(i) * m
    
    return answer