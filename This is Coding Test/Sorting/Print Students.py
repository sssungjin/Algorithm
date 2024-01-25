def solution(N, arr):
    for i in range(N):
        arr[i][1] = int(arr[i][1])
    arr = sorted(arr, key=lambda arr: arr[1])
    for i in arr:
        print(i[0], end=' ')

def main():
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(input().split())
    solution(N, arr)

if __name__ == "__main__":
    main()