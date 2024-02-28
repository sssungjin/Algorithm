n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]

time.sort(key = lambda x: (x[1], x[0]))

cnt = 1
end_time = time[0][1]

for i in range(1, n):
    # 회의 끝난 시간보다 시작시간이 더 늦다면
    if end_time <= time[i][0]:
        end_time = time[i][1]
        cnt += 1

print(cnt)