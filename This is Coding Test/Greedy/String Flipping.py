def solution(N):
    num0, num1 = 0, 0
    for i in range(len(N) - 1):
        if N[i] == 0 and N[i + 1] == 1:
            num0 += 1
        elif N[i] == 1 and N[i + 1] == 0:
            num1 += 1
    if N[-1] == 0:
        num0 += 1
    else: num1 += 1

    print(min(num0, num1))

def main():
    N = list(map(int, input()))
    solution(N)

if __name__ == "__main__":
    main()