def bigNumber(arr, M, k):
    arr.sort(reverse=True)
    first = arr[0]
    second = arr[1]

    ans = (first * k + second) * int(M/(k + 1))
    print(ans)
    ans += first * (M % (k + 1))
    print(ans)
    return ans



def main():
    N, M, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(bigNumber(arr, M, k))

if __name__ == "__main__":
    main()