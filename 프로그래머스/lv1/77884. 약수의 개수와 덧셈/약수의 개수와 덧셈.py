def solution(left, right):
    answer = 0
    flag = 0
    for i in range(left, right+1):
        for j in range(1, int(i**0.5)+1):
            if j * j == i:
                flag = 1
        if flag == 1:
            answer -= i
        else:
            answer += i
        flag = 0
    return answer