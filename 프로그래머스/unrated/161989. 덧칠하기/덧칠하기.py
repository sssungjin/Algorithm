def solution(n, m, section):
    answer = 0
    num = 0
    for i in section:
        if i > num:
            answer += 1
            num = i + m - 1
    return answer