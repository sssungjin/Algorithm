def f(number):
    
    # 짝수라면 가장 뒤에 있는 0을 1로 바꿈
    big = list('0' + bin(number)[2:])
    idx = ''.join(big).rfind('0')
    big[idx] = '1'
    
    # 홀수라면 가장 뒤에 있는 0을 1로 바꾸고 그 뒤에 1을 0으로 바꿈
    if number % 2 == 1:
        big[idx+1] = '0'
    
    return big

def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(int(''.join(f(num)), 2))
    return answer