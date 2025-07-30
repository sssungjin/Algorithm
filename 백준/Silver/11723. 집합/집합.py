import sys
input = sys.stdin.readline

n = int(input())
ans = set()
all = [str(i) for i in range(1, 21)]

for i in range(n):
    tmp = input().strip().split()
    
    if tmp[0] == 'add':
        ans.add(tmp[1])
    elif tmp[0] == 'remove':
        if tmp[1] in ans:
            ans.remove(tmp[1])
    elif tmp[0] == 'check':
        if tmp[1] in ans:
            print(1)
        else:
            print(0)
    elif tmp[0] == 'toggle':
        if tmp[1] in ans:
            ans.remove(tmp[1])
        else:
            ans.add(tmp[1])
    elif tmp[0] == 'all':
        ans.update(all)
    elif tmp[0] == 'empty':
        ans.clear()
    