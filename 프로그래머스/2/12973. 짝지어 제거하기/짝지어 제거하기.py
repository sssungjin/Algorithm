def solution(s):
    stk = []
    
    for i in s:
        if len(stk) == 0:
            stk.append(i)
        elif stk[-1] == i:
            stk.pop()
        else:
            stk.append(i)
            
    if len(stk):
        return 0
    else:
        return 1

