def solution(N):
    ans = 0
    for hour in range(N+1):
        for minute in range(60):
            for second in range(60):
                time = str(hour) + ':' + str(minute) + ':' + str(second)
                if '3' in time:
                    ans += 1
    print(ans)

def main():
    N = int(input())
    solution(N)

if __name__ == "__main__":
    main()