import itertools

def solution(N, M, arr):
    combi = itertools.combinations(arr, 2)
    ans = 0
    for i in combi:
        if i[0] != i[1]:
            ans += 1
    print(ans)

def main():
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    solution(N, M, arr)

if __name__ == "__main__":
    main()