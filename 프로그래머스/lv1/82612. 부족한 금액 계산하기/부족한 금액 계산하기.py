def solution(price, money, count):
    answer = 0
    total = 0
    for i in range(1,count+1):
        total += i * price
    if(money - total > 0):
        answer = 0
    else:
        answer = total - money
    return answer