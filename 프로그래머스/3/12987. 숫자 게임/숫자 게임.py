from collections import deque

def solution(A, B):
    answer = 0
    # B가 이길 때는 가장 작게 차이 나고
    # B가 질 때는 가장 크게 차이 나도록
    
    A.sort()
    B.sort()
    a_idx, b_idx = 0, 0
    
    # 1 3 5 7
    # 2 2 6 8
    while b_idx < len(B):
        if B[b_idx] > A[a_idx]:
            answer += 1
            b_idx += 1
            a_idx += 1
        elif B[b_idx] <= A[a_idx]:
            b_idx += 1
        
    return answer