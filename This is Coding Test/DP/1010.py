import math

def solution(n, m):
    ans = math.factorial(m) // (math.factorial(n) * math.factorial(m-n))
    return ans


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print(solution(n, m))