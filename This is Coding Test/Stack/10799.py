# 괄호 안에 바로 팝되는게 몇개가 있는지를 구함
op = input()
stack = []
cnt = 0

for i in range(len(op)):
    # 여는 기호라면 push
    if op[i] == '(':
        stack.append('(')
    else:
        # 현재 문자가 ) 이고 이전이 ( 이면 레이저임
        # 레이저 만나면 현재 쇠막대기 개수 더함
        if op[i - 1] == "(":
            stack.pop()
            cnt += len(stack)
        # 이전 문자가 ) 인 경우는 쇠막대기의 끝을 표현함
        else:
            stack.pop()
            cnt += 1

print(cnt)