def solution(n, s):
    if n > s:
        return [-1]
    
    answer = []
    
    base_value = s // n
    remainder = s % n
    
    answer = [base_value] * n
    
    # 마지막 값부터 넣어서 오름차순으로 만들기
    for i in range(remainder):
        answer[n - i - 1] += 1
    
    return answer