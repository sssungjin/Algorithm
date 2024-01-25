def binary_search2(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    # target이 중간값보다 작으면
    elif arr[mid] > target:
        # 시작값부터 중간값 - 1 범위를 탐색
        return binary_search2(arr, target, start, mid - 1)
    else:
        return binary_search2(arr, target, mid + 1, end)

def binary_search2(arr, target, start, end):
    while start <= end:
        mid  = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

def solution(N, arr, M, arr_find):
    # arr 배열에서 arr_find[i]가 있는지 확인
    for i in arr_find:
        if binary_search2(arr, i, 0, N-1) == None:
            print("no", end=' ')
        else:
            print("yes", end=' ')

def main():
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    M = int(input())
    arr_find = list(map(int, input().split()))
    solution(N, arr, M, arr_find)

if __name__ == "__main__":
    main()

# 2 3 7 8 9