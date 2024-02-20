t = int(input())
arr = [int(input()) for _ in range(t)]

def fibo(n):
    # 각각 0,1,2일때 0과1의 등장횟수 저장하는 변수
    # 0과1의 등장횟수도 피보나치 수열을 따름
    zeros = [1, 0, 1] # 1 0 1 1 2 3...
    ones = [0, 1, 1] # 0 1 1 2 3
    if n >= 3:
        for i in range(2, n):
            zeros.append(zeros[i-1] + zeros[i])
            ones.append(ones[i-1] + ones[i])
    print(f"{zeros[n]} {ones[n]}")

for i in arr:
    fibo(i)
    
    


