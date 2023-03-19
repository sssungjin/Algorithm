def solution(X, Y):
    answer = ''
    for i in range(9,-1,-1):
        answer = answer + min(X.count(str(i)), Y.count(str(i))) * str(i)
    if answer == '':
        return '-1'
    elif answer[0] == '0':
        return '0'
    return answer