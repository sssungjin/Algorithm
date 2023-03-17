def solution(number, limit, power):
    answer = 0
    attack = 0
    lst = []
    for i in range(1,number+1):
        attack = 0
        for j in range(1,int(i**(0.5))+1):
            if i % j == 0:
                attack += 1
                if((j**2) != i):
                    attack += 1
        if attack > limit:
            #lst.append(power)
            answer += power
        else:
            #lst.append(attack)
            answer += attack
    return answer