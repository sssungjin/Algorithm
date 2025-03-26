N, K = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0

def fun(order, num):
    global ans
    
    if order == len(str(N)):
        if not '0' in str(num):
            ans = max(ans, num)
        return
    
    for i in range(K):
        now_num = arr[i] * (10 ** (len(str(N)) - order - 1)) + num
        
        if now_num <= N:
            fun(order + 1, now_num)
        
        else:
            fun(order + 1, num)

fun(0, 0)

print(ans)
    