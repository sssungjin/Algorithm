def convert_to_base(n, base):
    chars = "0123456789ABCDEF"
    
    if n == 0:
        return "0"

    result = ""
    
    while n > 0:
        result = chars[n % base] + result
        n //= base
    return result
    
def solution(n, t, m, p):
    total = ""
    number = 0
    
    while len(total) < t * m:
        total += convert_to_base(number, n)
        number += 1
        
    answer = ""
    
    for i in range(len(total)):
        if i % m == p - 1:
            answer += total[i]
            if len(answer) == t:
                break
    
    return answer