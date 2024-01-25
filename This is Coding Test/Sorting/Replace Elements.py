def solution(N, M, arr_a, arr_b):
    ans = sum(arr_a)
    for i in range(M):
        ans -= min(arr_a)
        ans += max(arr_b)

    print(ans)

def main():
    N, M = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split())
    print(arr_a)
    print(arr_b)
    solution(N, M, arr_a, arr_b)

if __name__ == "__main__":
    main()