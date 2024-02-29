from itertools import combinations

heights = []
for _ in range(9):
    heights.append(int(input()))

total = 0

combi = list(combinations(heights, 7))
answer = []
for c in combi:
    if sum(c) == 100:
        answer.append(list(c))
        break

answer[0].sort()

for i in answer[0]:
    print(i)