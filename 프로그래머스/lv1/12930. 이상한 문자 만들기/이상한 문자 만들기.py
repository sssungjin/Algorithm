def solution(s):
    answer = []
    cnt = 0
    
    for i in s.split(' '):
        tmp = ''
        for j in range(len(i)):
            if j % 2:
                tmp += i[j].lower()
            else:
                tmp += i[j].upper()
        answer.append(tmp)
    return ' '.join(answer)