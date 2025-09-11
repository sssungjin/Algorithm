today = list(map(int, input().split()))
d_day = list(map(int, input().split()))



# 윤년(True)이면 366일
def is_leap(year):
    # 4로 나눠지면 윤년
    if year % 4 == 0:
        # 4로 나눠지고 400으로 안나눠지면서 100으로 나눠지면 평년
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False


def year_to_day(year):
    day = 0
    for i in range(1, year):
        if is_leap(i):
            day += 366
        else:
            day += 365
    
    return day

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
        
is_gg = False
if d_day[0] - today[0] > 1000:
    is_gg = True
elif d_day[0] - today[0] == 1000 and (d_day[1] > today[1] or (d_day[1] == today[1] and d_day[2] >= today[2])):
    is_gg = True

if is_gg:
    print("gg")
else:
    today_day = year_to_day(today[0]) + month_to_day(today[0], today[1]) + today[2]
    d_day_day = year_to_day(d_day[0]) + month_to_day(d_day[0], d_day[1]) + d_day[2]
    print("D-" + str(d_day_day - today_day))
