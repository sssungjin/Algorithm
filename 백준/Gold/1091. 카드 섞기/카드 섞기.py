N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))

arr = [0, 1, 2] * (N // 3)
ori = P
new = [0] * N
ans = 0

while P != arr:
    
    for i in range(N):
        new[S[i]] = P[i]
    
    P = new
    new = [0] * N
    
    ans += 1
    if ori == P:
        ans = -1
        break
    
print(ans)