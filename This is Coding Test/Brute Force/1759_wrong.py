from itertools import combinations

l, c = map(int, input().split())
alpha = list(input().split())
mom, son = [], []
ans = []
# 모음이면 True
def check(c):
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        return True
    else:
        return False

# 모음과 자음을 먼저 나눈다.
for i in alpha:
    if check(i):
        mom.append(i)
    else:
        son.append(i)
        
for i in range(1, l-1):
    # 모음 총 개수
    mom_combi = combinations(mom, i)
    for a in mom_combi:
        son_combi = combinations(son, l-i)
        for b in son_combi:
            ans.append(''.join(a) + ''.join(b))

ans1 = []
for i in ans:
    s1 = ''.join(sorted(i))
    ans1.append(s1)

for i in ans1:
    print(i)
