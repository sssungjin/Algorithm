def solution(N, arr):
    c = sorted(arr, reverse = True)

    for i in c:
        print(i, end=" ")
    

def main():
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    solution(N, arr)

if __name__ == "__main__":
    main()