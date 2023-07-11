def solution(numbers):
    answer = [-1] * len(numbers)
    stk = []
    for i in range(len(numbers)):
        #스택->인덱스 삽입
        #인덱스 통해 현재 값과 비교해서 현재 값이 크면 해당 인덱스에 삽입
        while stk and numbers[stk[-1]] < numbers[i]:
            answer[stk.pop()] = numbers[i]
        stk.append(i)
    return answer