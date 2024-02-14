from collections import deque

# 최소 균형 문자열의 인덱스 반환
def balanced_idx(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        elif p[i] == ')':
            cnt -= 1
        if cnt == 0:
            return i
# 올바른지 확인
def right_check(p):
    queue = deque()
    for i in p:
        if len(queue) == 0 and i == ')':
            return False
        if i == '(':
            queue.append(i)
        elif i == ')':
            queue.pop()
    if len(queue) == 0:
        return True
    else: return False
                
    
def solution(p):
    answer = ''
    if p == '':
        return ''
    
    # u,v는 균형, u는 최소 균형
    idx = balanced_idx(p)
    u = p[:idx+1]
    v = p[idx+1:]
    # 올바르면 u 붙이고 v는 다시 처음부터 돌림
    if right_check(u):
        answer = u + solution(v)
    # u가 올바르지 않다면
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        # 첫, 마지막 제거 후 반대로 바꾸기
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        # v + u
        answer += "".join(u)
    return answer