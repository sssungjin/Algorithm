def solution(N):
    dp = [0] * 1001
    dp[1] = 1
    dp[2] = 3
    for i in range(3, N + 1):
        dp[i] = dp[i-1] + dp[i-2] * 2
    print(dp[N])

def main():
    N = int(input())
    solution(N)

if __name__ == "__main__":
    main()