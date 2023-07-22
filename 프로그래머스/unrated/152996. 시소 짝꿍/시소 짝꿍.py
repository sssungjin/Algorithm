from collections import Counter

def solution(weights):
    answer = 0
    count = Counter(weights)
    ratio = [3/2, 4/2, 4/3]
    for item, cnt in count.items():
        if cnt > 1:
            answer += cnt * (cnt-1) // 2
            
    weights = list(set(weights))
    
    for weight in weights:
        for r in ratio:
            if weight * r in weights:
                answer += count[weight] * count[weight * r]
    return answer