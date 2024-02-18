n = int(input())
data = []
time, pay = [], []

for i in range(n):
    t, p = map(int, input().split())
    data.append((t, p))
    time.append(t)
    pay.append(p)

dp = [0 for _ in range(n + 1)]

for i in range(n-1, -1, -1):
    # 상담기간이 퇴사일을 넘어가는 경우
    if time[i] + i > n:
        # 다음날의 금액과 같음
        dp[i] = dp[i + 1]
    # 오늘 상담을 안한 경우( = 다음날의 금액과 같음)와 상담을 한 경우를 비교
    else:
        dp[i] = max(dp[i+1], dp[time[i] + i] + pay[i])

print(dp[0])