e, s, m = map(int, input().split())
ans = 0

while not(e == 1 and s == 1 and m == 1):
    if e == 0:
        e = 15
    if s == 0:
        s = 28
    if m == 0:
        m = 19
    e -= 1
    s -= 1
    m -= 1
    ans += 1

print(ans+1)