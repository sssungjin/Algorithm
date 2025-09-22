import sys
import math

input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
answer = 0

for i in range(N):
    # 총 감독관은 무조건 1명 존재
    A[i] -= B
    answer += 1


    # 총감독관 뺀 값이 0보다 크면 부감독관 필요
    if A[i] > 0:
        # 부감독관은 math.ceil(A[i] / C) 만큼 필요
        answer += math.ceil(A[i] / C)

print(answer)
