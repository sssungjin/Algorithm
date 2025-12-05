def solution(s):
    answer = 0
    while s:
        x = s[0]
        x_cnt = 0
        other_cnt = 0
        tmp = ''
        for i in range(len(s)):
            char = s[i]
            if char == x:
                x_cnt += 1
            else:
                other_cnt += 1
            
            if x_cnt == other_cnt:
                tmp = s[i+1:]  
                answer += 1
                break
            elif x_cnt != other_cnt and i == len(s) - 1:
                answer += 1
                break
        s = tmp
        
    return answer