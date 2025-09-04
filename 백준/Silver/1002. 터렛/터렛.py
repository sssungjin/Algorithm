# a의 좌표 x, y 와 a와 t까지의 거리 r
# b의 좌표 x, y와 b와 t까지의 거리 r
# 위 정보를 가지고 t의 가능한 좌표를 모두 구하기 

# 겹치면 2, 맞닿으면 1, 떨어져있거나 안에 있으면 0, 일치하면 무한대
# 케이스별로 구하기
# 겹치는 경우를 else
# 맞닿는 경우, 떨어져있거나 안에있는 경우, 일치하는 경우 구하기 쉬움 




import sys
import math

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().strip().split())

    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
    if distance == 0 and r1 == r2:
        print(-1)
    elif abs(r1 - r2) == distance or r1 + r2 == distance:
        print(1)
    elif abs(r1 - r2) < distance < (r1 + r2):
        print(2)
    else:
        print(0)
        