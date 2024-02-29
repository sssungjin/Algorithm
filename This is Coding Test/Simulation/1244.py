# 남: 스위치 번호가 자기가 받은 수의 배수이면 상태 바꿈
# 여: 자기 번호 기준으로 가능한 대칭 사이를 바꿈 

n = int(input())
switch = [-1] + list(map(int, input().split()))
num = int(input())

for i in range(num):
    # 남자
    gender, number = map(int, input().split())
    if gender == 1:
        for j in range(number, n + 1, number):
            if switch[j] == 1:
                switch[j] = 0
            else:
                switch[j] = 1
    # 여자
    else:
        if switch[number] == 0:
            switch[number] = 1
        else:
            switch[number] = 0
        left, right = number - 1, number + 1
        while left > 0 and right <= n and switch[left] == switch[right]:
            if switch[left] == 0:
                switch[left], switch[right] = 1, 1
            else:
                switch[left], switch[right] = 0, 0
            left = left - 1
            right = right + 1

for i in range(1, n+1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()