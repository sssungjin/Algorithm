import math

def solution(n, stations, w):
    answer = 0
    current_pos = 1
    
    for station in stations:
        if station - w > 0:
            coverage_start = station - w
        else:
            coverage_start = 1
        
        # 현재 보고 있는 아파트의 번호가 커버해야할 범위 시작점보다 앞에 있다면
        # current_pos ~ coverage_start - 1 까지 비어있음
        if current_pos < coverage_start:
            # 빈 구간의 길이 
            L = coverage_start - current_pos
            
            num_needed = math.ceil(L / (2 * w + 1))
            
            answer += num_needed
        current_pos = station + w + 1
        
    if current_pos <= n:
        L = n - current_pos + 1
        
        num_needed = math.ceil(L / (2 * w + 1))
        answer += num_needed
        
    return answer