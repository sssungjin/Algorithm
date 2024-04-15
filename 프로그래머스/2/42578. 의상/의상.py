from collections import defaultdict

def solution(clothes):
    answer = 1
    dic = dict()
    int_dict = defaultdict(int)
    
    for cloth in clothes:
        int_dict[cloth[1]] += 1
    
    for i in int_dict:
        answer *= int_dict[i] + 1
    
    return answer-1