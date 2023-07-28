def solution(num_list):
    answer = -1
    for i in num_list:
        if i < 0:
            return num_list.index(i)
    return answer