import itertools
def operation(n, m, op):
    if op == '*':
        return str(int(n) * int(m))
    elif op == '+':
        return str(int(n) + int(m))
    elif op == '-':
        return str(int(n) - int(m))
    
def calculate(expression, op):
    #op로 구분해서 다 잘라줌
    tmp, arr = '', []
    for i in expression:
        if i.isdigit():
            tmp += i
        else:
            arr.append(tmp)
            arr.append(i)
            tmp = ''
    arr.append(tmp)
    
    #우선순위 순열로 만든거 기준으로 계산해서 반환
    for o in op:
        stack = []
        while len(arr) != 0:
            tmp = arr.pop(0)
            if tmp == o:
                stack.append(operation(stack.pop(), arr.pop(0), tmp))
            else:
                stack.append(tmp)
        arr = stack
    return abs(int(arr[0]))

def solution(expression):
    op = list(itertools.permutations(['*', '+', '-'], 3))
    result = []
    for o in op:
        result.append(calculate(expression, o))
    return max(result)