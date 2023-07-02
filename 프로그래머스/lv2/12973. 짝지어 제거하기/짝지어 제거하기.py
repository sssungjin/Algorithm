def solution(s):
    answer = 0
    stk = []
    for i in s:
        if len(stk) == 0:
            stk.append(i)
        elif stk[-1] == i:
            stk.pop()
        else:
            stk.append(i)
    if len(stk) == 0:
        return 1
    else: 
        return 0
    return answer
