s = list(input())
stk = []
for _ in range(int(input())):
    cmd = list(input().split())
    if cmd[0] == 'L':
        if s:
            stk.append(s.pop())
    elif cmd[0] == 'D':
        if stk:
            s.append(stk.pop())
    elif cmd[0] == 'B':
        if s:
            s.pop()
    else:
        s.append(cmd[1])

s.extend(reversed(stk))
print(''.join(s))

# abcdx
# 3