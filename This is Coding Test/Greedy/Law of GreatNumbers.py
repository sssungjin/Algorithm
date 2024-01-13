def bigNumber(arr, M, k):
    mCnt, idx, ans = 0, 0, 0
    arr.sort(reverse=True)

    for i in range(0, M):
        if mCnt == k:
            ans += arr[idx+1]
            print(arr[idx+1])
            mCnt = 0
        else:
            ans += arr[idx]
            print(arr[idx])
            mCnt += 1
        #print(ans)
    return ans

def main():
    N, M, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(bigNumber(arr, M, k))

if __name__ == "__main__":
    main()