def solution(N, arr):
    arr.sort()
    ans = 1
    for i in arr:
        if ans < i:
            break
        ans += i
    print(ans)

def main():
    N = int(input())
    arr = list(map(int, input().split()))
    solution(N, arr)

if __name__ == "__main__":
    main()