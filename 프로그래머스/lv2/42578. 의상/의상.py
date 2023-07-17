def solution(clothes):
    answer = 1
    closet = {}
    
    for cloth, body in clothes:
        closet[body] = closet.get(body, 0) + 1
        
    for i in closet:
        answer *= closet[i] + 1
        
    return answer-1