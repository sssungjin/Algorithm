# 안에 있으면 곱하기
# 그냥 붙어 있으면 더하기

# 안에 아무것도 없는것부터 순서대로
# [를 스택에 넣고 ]만나면 pop 시킴
# (()pop[[]POP]POP)pop([])ㅁ
# 계산 순서를 매칭 시키는게 포인트
# (()[[]])([])
# (2 + (3 * 3))  * 2
# (2 + (3 + 0) * 3) * 2 + 3 * 2
# 들어가자마자 pop 되는데 뒤에 있는게 여는 기호 [, ( 라면 +
# 들어가자마자 pop 되는데 뒤에 있는게 닫는 기호 ], ) 라면 아무것도 안붙임
# 들어가자마자 pop 되지 않았다면 pop 될 때 * 숫자 붙임

s = list(input())

def sol(s):
    stk = []
    ans = 0
    tmp = 1

    for i in range(len(s)):
        if s[i] == '(':
            stk.append(s[i])
            tmp *= 2
        elif s[i] == '[':
            stk.append(s[i])
            tmp *= 3
        elif s[i] == ')':
            if not stk or stk[-1] == '[':
                ans = 0
                break
            if s[i-1] == '(':
                ans += tmp
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