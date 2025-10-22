def solution(n, times):
    left = 1
    right = max(times) * n 
    answer = right

    while left <= right:
        mid = (left + right) // 2
        
        # 4. Calculate total people processed within 'mid' time
        processed_people = 0
        for time in times:
            # mid는 주어진 시간, time은 한 심사관이 평가하는데 걸리는 시간
            # 각 심사관이 주어진 시간동안 몇명을 심사할 수 있는지
            processed_people += mid // time
            if processed_people >= n:
                break
                
        if processed_people >= n:
            answer = mid 
            right = mid - 1
        else:
            left = mid + 1
            
    return answer

