import math

def solution(n, k):
    answer = []
    people = [i for i in range(1, n + 1)]
    
    for i in range(1, n + 1):
        divider = math.factorial(n-i)
        idx = k // divider
        if k % divider == 0:
            idx -= 1
        
        answer.append(people[idx])
        people.pop(idx)
        k -= idx * divider
        
    return answer
        