# 맨 앞자리수를 가장 크게 만들고 가장 작은 값들 제거

def solution(number, k):
    answer = []
    
    for i in number:
        while k > 0 and answer and answer[-1] < i:
            answer.pop()
            k -= 1
        answer.append(i)
        
    return ''.join(answer[:len(answer) - k])