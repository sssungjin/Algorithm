
s = list(input())

def sol(s):
    stk = []
    ans = 0
    tmp = 1

    for i in range(len(s)):
        # 만약 (( 이렇게 연속으로 만나면 tmp는 2 * 2 가 되고 
        # )를 만나면 ans에 2*2 더하고 tmp는 2가 되고 
        # )를 또 만나면 s[i-1]이 (이 아니기 때문에 더하지 않고 tmp 2 나눠서 1이 됨
        if s[i] == '(':
            stk.append(s[i])
            tmp *= 2
        elif s[i] == '[':
            stk.append(s[i])
            tmp *= 3
        elif s[i] == ')':
            # 틀린 괄호
            if not stk or stk[-1] == '[':
                ans = 0
                break
            # s[i-1] '(' s[i] ')' 인 경우는 계산한 tmp 값을 더해줌
            if s[i-1] == '(':
                ans += tmp
            # 한번 ()에 대한 계산 했으므로 2 나눠줌
            tmp //= 2
            stk.pop()
        else:
            if not stk or stk[-1] == '(':
                ans = 0
                break
            if s[i-1] == '[':
                ans += tmp
            tmp //= 3
            stk.pop()
    if stk:
        ans = 0
    return ans

print(sol(s))