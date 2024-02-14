from itertools import permutations

n = int(input())
num = list(map(int, input().split()))
oper = list(map(int, input().split()))
length = sum(oper)
oplist = []
op = ['+', '-', '*', '/']

for i in range(4):
    for j in range(oper[i]):
        oplist.append(op[i])

permu = list(permutations(oplist, length))

ans = []
for ops in permu:
    tmp = 0
    for j in range(length):
        if j == 0:
            if ops[j] == '+':
                tmp = num[0] + num[1]
            elif ops[j] == '-':
                tmp = num[0] - num[1]
            elif ops[j] == '*':
                tmp = num[0] * num[1]
            elif ops[j] == '/':
                tmp = int(num[0]/num[1])
        else:
            if ops[j] == '+':
                tmp += num[j+1]
            elif ops[j] == '-':
                tmp -= num[j+1]
            elif ops[j] == '*':
                tmp *= num[j+1]
            elif ops[j] == '/':
                tmp = int(tmp/num[j+1])
    ans.append(tmp)
print(max(ans))
print(min(ans))