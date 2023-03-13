def solution(seoul):
    answer = ''
    tmp = 0
    for i in seoul:
        if i == "Kim":
            answer = "김서방은 %d에 있다" %tmp
        tmp += 1
    return answer