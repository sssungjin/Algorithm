n = int(input())
time = list(map(int, input().split()))
# 0번 3, 1번 1, 2번 4, 3번 3, 4번 2

# 시간, 인덱스
time_info = []
for i in range(n):
    time_info.append((time[i], i))

time_info.sort()
total = 0
for i in range(n):
    for j in range(i+1):
        total += time_info[j][0]

print(total)