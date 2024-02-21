from collections import deque

def solution(arr, num, op):
    # [, ] 자르기
    arr = arr[1:-1]
    # , 기준으로 잘라서 배열에 저장
    arr = arr.split(',')
    q = deque(arr)
    rev = 0
    
    if num == 0:
        q = []

    # 숫자의 개수가 D보다 적다면? error
    if num < op.count('D'):
        print("error")
        return
    
    for j in op:
        # reverse count +1
        if j == 'R':
            rev += 1
        # D인 경우 지금까지의 rev를 짝수번 하면 앞에꺼 pop, 홀수면 뒤에꺼 pop
        elif j == 'D':
            if rev % 2 == 0:
                q.popleft()
            else:
                q.pop()

    if rev % 2 == 0:
        print("[" + ",".join(q) + "]")
    else:
        q.reverse()
        print("[" + ",".join(q) + "]")
            

t = int(input())
ans = []
for _ in range(t):
    op = input()
    num = int(input())
    arr = input()
    solution(arr, num, op)