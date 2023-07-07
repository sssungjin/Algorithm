def solution(a, b):
    answer = ''
    요일 = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    day = 0
    for i in range(1,a):
        if i in [1, 3, 5, 7, 8, 10, 12]:
            day += 31
        elif i == 2:
            day += 29
        else: day += 30
    day += b
    answer = 요일[day%7-1]
    return answer