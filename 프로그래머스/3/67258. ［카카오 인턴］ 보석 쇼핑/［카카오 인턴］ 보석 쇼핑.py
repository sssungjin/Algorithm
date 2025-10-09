def solution(gems):
    num_gems_total = len(set(gems)) # 전체 보석 종류의 수
    n = len(gems)
    
    answer = [0, n]
    
    start, end = 0, 0
    
    # 현재 구간에 포함된 보석의 종류와 개수를 저장할 딕셔너리
    gem_counts = {gems[0]: 1}

    # 투 포인터 이동 시작
    while start < n and end < n:
        # 현재 구간([start, end])이 모든 보석을 포함하는 경우
        if len(gem_counts) == num_gems_total:
            if (end - start) < (answer[1] - answer[0]):
                answer = [start + 1, end + 1]
            
            
            gem_counts[gems[start]] -= 1 # 현재 포인터 보석은 -1
            if gem_counts[gems[start]] == 0:
                del gem_counts[gems[start]] # 개수가 0이 되면 딕셔너리에서 제거
            start += 1
        
        else:
            # end 포인터를 오른쪽으로 이동
            end += 1
            if end == n:
                break
            
            gem_counts[gems[end]] = gem_counts.get(gems[end], 0) + 1
            
    return answer