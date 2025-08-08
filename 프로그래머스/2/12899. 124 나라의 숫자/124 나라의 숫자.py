def solution(n):
    answer = ''
    
    # 나머지가 1이면 1, 2면 2, 0이면 4(몫을 1 마이너스)
    while n > 0:
        mod = n % 3
        n = n // 3
        
        if mod == 0:
            mod = 4
            n -= 1
        answer = str(mod) + answer
        
    return answer