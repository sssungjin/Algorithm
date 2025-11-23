import math

def solution(w,h):
    unusable = w + h - math.gcd(w, h)
    answer = w * h - unusable
    return answer