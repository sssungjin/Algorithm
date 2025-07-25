# N은 기존 점수의 개수
# 두번째는 태수의 점수
# P는 랭킹 인정 등수

import sys
input = sys.stdin.readline

n, taesu, p = map(int, input().split())
if n > 0:
    scores = list(map(int, input().split()))
else:
    scores = []

rank = 1 

if n == 0:
    print(1)
else:
    for i in range(n):
        if scores[i] > taesu:
            rank += 1
        else:
            break
    
    if n == p and taesu <= scores[-1]:
        print(-1)
    else:
        print(rank)
