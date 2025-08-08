from itertools import combinations 
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course:
        combi_list = []
        for order in orders:
            order = sorted(order)
            if len(order) >= c:
                combi_list += combinations(order, c)
    
        combi_count = Counter([''.join(combi) for combi in combi_list])
        
        if combi_count:
            max_count = max(combi_count.values())
            if max_count >= 2:
                for menu, cnt in combi_count.items():
                    if cnt == max_count:
                        answer.append(menu)
    
    return sorted(answer)