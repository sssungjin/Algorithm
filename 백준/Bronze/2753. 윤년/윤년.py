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
    
n = int(input())

if is_leap(n):
    print("1")
else:
    print("0")