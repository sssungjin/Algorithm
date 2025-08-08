import math
from functools import reduce
# reduce(math.gcd, arr)

def solution(arrayA, arrayB):
    answer = 0
    # 1. arrayA 에 있는 모든 수를 나눌 수 있는 수 and arrayB에 있는 모든 수를 나눌 수 없는 수 중에 큰 수
    # 2. 1번과 반대
    
    # arrayA의 최대공약수, arrayB의 최대공약수 구하기
    # 각 최대공약수의 약수 구함
    # arrayA의 최대공약수의 모든 약수로 arrayB 나눠보고 안나눠지는 가장 큰 수 구하기
    # arrayB의 최대공약수의 모든 약수로 arrayA 나눠보고 안나눠지는 가장 큰 수 구하기
    
    a_divisiors = get_common_divisors(arrayA)
    b_divisiors = get_common_divisors(arrayB)

    print(a_divisiors)
    print(b_divisiors)
    
    for num in a_divisiors:
        for i in arrayB:
            if i % num == 0:
                break
        else:
            answer = max(answer, num)
            
    for num in b_divisiors:
        for i in arrayA:
            if i % num == 0:
                break
        else:
            answer = max(answer, num)
    return answer


def get_common_divisors(numbers):
    # gcd 구하기
    gcd_all = reduce(math.gcd, numbers)
    
    # gcd의 약수들 구하기
    divisors = []
    for i in range(2, gcd_all + 1):
        if gcd_all % i == 0:
            divisors.append(i)
    return divisors
    