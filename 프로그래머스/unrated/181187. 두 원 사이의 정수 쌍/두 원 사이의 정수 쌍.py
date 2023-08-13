from math import sqrt, floor

def solution(r1, r2):
    answer = 0
    for i in range(0, r1):
        answer += floor(sqrt(r2**2 - i**2)) - floor(sqrt(r1**2 - i**2 - 1))
    for i in range(r1, r2):
        answer += floor(sqrt(r2**2 - i**2))
    return answer * 4