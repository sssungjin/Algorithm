def solution(N):
    alpha, digit = [], []
    for i in N:
        if i.isalpha():
            alpha.append(i)
        else:
            digit.append(int(i))
    alpha.sort()
    ans = ''.join(alpha)
    ans += str(sum(digit))
    print(ans)

def main():
    N = input()
    solution(N)

if __name__ == "__main__":
    main()