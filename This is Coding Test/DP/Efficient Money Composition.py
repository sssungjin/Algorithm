def solution(N, M, arr):
    dp = [10001] * 20
    dp[0] = 0

    for i in arr:
        for j in range(i, M + 1):
            if dp[j - i] != 10001:
                dp[j] = min(dp[j], dp[j - i] + 1)
    print(dp)
    if dp[M] == 10001:
        print(-1)
    else: print(dp[M])

def main():
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    solution(N, M, arr)

if __name__ == "__main__":
    main()