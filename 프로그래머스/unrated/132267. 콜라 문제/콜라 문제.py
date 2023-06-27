def solution(a, b, n):
    answer = 0
    while(n >= a):
        coke = n % a
        n = n // a * b
        answer += n
        n += coke
    return answer