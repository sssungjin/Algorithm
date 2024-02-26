# 12345
# 21232425
# 3311224455
def solution(answers):
    answer = []
    su1 = [1,2,3,4,5] * 2000 
    su2 = [2,1,2,3,2,4,2,5] * 1250
    su3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    cnt = [0] * 3
    
    for i in range(len(answers)):
        if su1[i] == answers[i]:
            cnt[0] += 1
        if su2[i] == answers[i]:
            cnt[1] += 1
        if su3[i] == answers[i]:
            cnt[2] += 1
        
    max_cnt = max(cnt)
    for i in range(3):
        if max_cnt == cnt[i]:
            answer.append(i + 1)
    
    return answer