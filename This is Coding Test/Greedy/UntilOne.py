def until(N, K):
    ans = 0
    while N != 1:
        if N < K:
            ans += 1
            N -= 1
        else:
            ans += N % K    
            ans += 1        
            N = N // K
    return ans

def main():
    N, K = map(int, input().split())
    print(until(N, K))

if __name__ == "__main__":
    main()