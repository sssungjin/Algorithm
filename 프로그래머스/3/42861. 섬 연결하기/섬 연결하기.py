def solution(n, costs):
    answer = 0
    # costs 에는 번호, 번호, 비용
    costs.sort(key = lambda x: (x[2]))
    
    link = set([costs[0][0]])
    
    while len(link) != n:
        for v in costs:
            # 이어져있음 
            if v[0] in link and v[1] in link:
                continue
            # 하나만 있다면
            if v[0] in link or v[1] in link:
                answer += v[2]
                link.update([v[0], v[1]])
                break
                
    return answer