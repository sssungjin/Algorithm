exp = input().split('-')
num = []

for i in exp:
    sum = 0
    tmp = i.split('+')
    for j in tmp:
        sum += int(j)
    num.append(sum)

# 첫번째꺼는 +임 이후로는 -
answer = num[0]

for i in range(1, len(num)):
    answer -= num[i]
print(answer)