def solution(N, M, arr_a, arr_b):
    arr_a.sort() # 오름차순
    arr_b.sort(reverse = True) # 내림차순
    for i in range(M):
        if arr_b[i] > arr_a[i]:
            arr_a[i], arr_b[i] = arr_b[i], arr_a[i]

    print(sum(arr_a))

def main():
    N, M = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))

    solution(N, M, arr_a, arr_b)

if __name__ == "__main__":
    main()