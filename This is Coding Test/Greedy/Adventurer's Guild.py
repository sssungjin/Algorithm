def solution(N, fear):
    ans = 0
    fear.sort()
    while fear:
        big = fear.pop()
        # 남아 있는 모험가가 더 많으면 그룹에 추가할 수 있음
        if len(fear) >= (big - 1):
            for i in range(big - 1):
                fear.pop()
            ans += 1

    print(ans)

def main():
    N = int(input())
    fear = list(map(int, input().split()))
    solution(N, fear)


if __name__ == "__main__":
    main()