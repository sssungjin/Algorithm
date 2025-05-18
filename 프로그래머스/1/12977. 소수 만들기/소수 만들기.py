from itertools import combinations
import math


def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

# 3000 이하의 소수
def solution(nums):
    answer = 0
    
    combi = list(combinations(nums, 3))
    
    for i in combi:
        if is_prime(sum(i)):
            answer += 1
    
    return answer