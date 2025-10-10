def can_cross(stones, k, n):
    
    zero_count = 0
    for stone in stones:
        if stone - n < 0:
            zero_count += 1
        else:
            zero_count = 0
        
        if zero_count >= k:
            return False
        
    return True


def solution(stones, k):
    answer = 0
    
    left = 1
    right = 200000000
    
    while left <= right:
        mid = (left + right) // 2
        
        if can_cross(stones, k, mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return answer