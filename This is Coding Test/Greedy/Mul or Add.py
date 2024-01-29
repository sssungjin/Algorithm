def solution(N):
    ans = N[0]
    for i in range(1, len(N)):
        ans = max(ans + N[i], ans * N[i])
    print(ans)

def main():
    N = list(map(int, input()))
    solution(N)

if __name__ == "__main__":
    main()