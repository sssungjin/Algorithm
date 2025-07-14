from collections import deque
n = int(input())

cmds = [input() for _ in range(n)]
stack = deque()

for cmd in cmds:
    i = cmd.split()
    if i[0] == 'push':
        stack.append(i[1])
    if i[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
            continue
    if i[0] == 'size':
        print(len(stack))
    if i[0] == 'empty':
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    if i[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
            continue