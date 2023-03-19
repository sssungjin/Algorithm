def solution(food):
    answer = '0'
    for i,cnt in enumerate(food[:0:-1]):
        tmp = len(food) - i - 1
        answer = cnt//2 * str(tmp) + answer + cnt//2 * str(tmp)
    return answer