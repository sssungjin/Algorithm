from itertools import permutations

def is_prime(x): #x가 소수인지 확인
    for i in range(2, x):
    	if x % i == 0:
        	return False
    return True

def solution(numbers):
    answer = []
    number = []
    nums = [n for n in numbers]
    permu = []
    for i in range(1, len(numbers) + 1):
        permu += list(permutations(nums, i))
        
    new_nums = [int("".join(p)) for p in permu]
    
    for n in new_nums:
        if n < 2:
            continue
        flag = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                flag = False
                break
        if flag:
            answer.append(n)
            
    return len(set(answer))