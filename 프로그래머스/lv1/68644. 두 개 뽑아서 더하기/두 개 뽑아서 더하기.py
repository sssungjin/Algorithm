from itertools import combinations

def solution(numbers):
    answer = []
    c_list = list(combinations(numbers,2))
    for i in range(len(c_list)):
        for combi in c_list:
            answer.append(sum(combi))
    res = list(set(answer))
    res.sort()
    
    return res