def solution(N, M, arr):
    start = 0
    end = max(arr)

    result = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2
        # 잘린 떡 길이 구하기
        for i in arr:
            if i > mid:
                total += i - mid
        if total < M:
            # M보다 작다면 절단기를 줄여야 한다.
            end = mid - 1
        else:
            # M보다 큰거는 일단 조건은 만족한것이기 때문에 mid 값 저장
            result = mid
            start = mid + 1
    print(result)

def main():
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    solution(N, M, arr)

if __name__ == "__main__":
    main()