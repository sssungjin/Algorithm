def solution(N):
    dp = [0] * 30001

    for i in range(2, N + 1):
        if i % 5 == 0:
            dp[i] = min(dp[i // 5] + 1, dp[i - 1] + 1)
        elif i % 3 == 0:
            dp[i] = min(dp[i // 3] + 1, dp[i - 1] + 1)
        elif i % 2 == 0:
            dp[i] = min(dp[i // 2] + 1, dp[i - 1] + 1)
        else:
            dp[i] = dp[i - 1] + 1

    print(dp[N])        

def main():
    N = int(input())
    solution(N)

if __name__ == "__main__":
    main()