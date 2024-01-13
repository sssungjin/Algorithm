def numberCard(arr, N):
    extractArr = []
    for i in range(len(arr)):
        extractArr.append(min(arr[i]))
    return max(extractArr)

def main():
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)] # 2차원 배열 입력
    print(numberCard(arr, N))

if __name__ == "__main__":
    main()