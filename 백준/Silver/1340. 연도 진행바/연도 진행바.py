# 날짜 윤년 계산해서 (month-1) * (28,29,30,31) + day
# 시간 


# 하루 에서 12시간이면 12/24 = 0.5일
# 시간 + 분/60


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False
    
    
def time_to_day(hour, minute):
    return (hour + minute/60) / 24

def month_to_day(year, month):
    day = 0
    for i in range(1, month):
        if  i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
            day += 31
        elif i == 2:
            if is_leap(year):
                day += 29
            else:
                day += 28
        else:
            day += 30
    
    return day
                
    

def convert_month(month):
    if month == 'January':
        return 1
    elif month == 'February':
        return 2
    elif month == 'March':
        return 3
    elif month == 'April':
        return 4
    elif month == 'May':
        return 5
    elif month == 'June':
        return 6
    elif month == 'July':
        return 7
    elif month == 'August':
        return 8
    elif month == 'September':
        return 9
    elif month == 'October':
        return 10
    elif month == 'November':
        return 11
    elif month == 'December':
        return 12
    
info = list(input().split())

def calculate_percent(info):
    month = convert_month(info[0])
    year = int(info[2])
    date = int(info[1][:-1])
    hour = int(info[3][:2])
    minute = int(info[3][3:5])

    isLeap = is_leap(year)
    
    total = month_to_day(year, month) + date - 1 + time_to_day(hour, minute)
    
    if isLeap:
        print(total / 366 * 100)
    else:
        print(total / 365 * 100)


calculate_percent(info)