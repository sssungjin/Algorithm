import math
def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True
    
# n을 k진수로 변환
# 변환한 수에서 나올 수 있는 모든 수를 찾음
# 211010 이라면 
# 2, 21, 211, 2110, 21101, 211010
# 1, 11, 110, 1101, 11010
# 1, 10, 101, 1010
# 0, 01, 010,
# 1, 10
# 위 문자열에서 조건을 만족하는 문자열 저장
# 1. 아무것도 없는 경우는 전체 211010 을 체크함
# 2. 시작 또는 끝에 0이 있는 모든 문자열 저장 -> 2110, 211010, 110, 11010, 10, 1010, 01, 010, 10
# 위 문자열에서 시작 또는 끝의 0을 제거했을 때 소수인지 확인

def convert(n, k):
    result = ""
    while n > 0:
        result = str(n % k) + result
        n //= k
        print(result)
    return result

# 1. 아무것도 없는 경우는 전체 211010 을 체크함
# 2. 시작 또는 끝에 0이 있는 모든 문자열 저장 -> 2110, 211010, 110, 11010, 10, 1010, 01, 010, 10


def solution(n, k):
    n_base_k = convert(n, k)
    candidates = n_base_k.split('0')  # 0을 기준으로 분리
    
    print(candidates)

    count = 0
    for token in candidates:
        if token and is_prime(int(token)):
            count += 1
    return count