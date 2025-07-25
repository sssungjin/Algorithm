import sys
input = sys.stdin.readline

n = int(input())
number = []
for i in range(n):
    number.append(input().strip())

for i in range(len(number[0])):
    new_number = set()
    flag = True
    for j in range(n):
        if number[j][-(1 + i):] not in new_number:
            new_number.add(number[j][-(1 + i):])
            #print(number[j][-(1 + i):])
        else:
            flag = False
            break
    if flag:
        ans = i + 1
        break
        
print(ans)