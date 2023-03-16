def solution(before, after):
    answer = 0
    a = sorted(list(before))
    b = sorted(list(after))
    if a == b:
        answer = 1
    return answer