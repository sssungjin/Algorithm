import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

if N == 1:
    print("A")
    sys.exit()

if N == 2:
    if arr[0] == arr[1]:
        print(arr[0])
    else:
        print("A")
    sys.exit()

# N > 2 일 때
x1, x2, x3 = arr[0], arr[1], arr[2]

# a를 구하기 위한 분모 (x2 - x1)
denominator = x2 - x1

# 분모가 0일 때 (x1 == x2)
if denominator == 0:
    if x3 == x2:
        a = 1
        b = 0
    else:
        print("B")
        sys.exit()
else:
    # a가 정수인지 확인
    if (x3 - x2) % denominator != 0:
        print("B")
        sys.exit()
    a = (x3 - x2) // denominator

# b를 계산
b = x2 - x1 * a

# 찾은 규칙(a, b)이 수열 전체에 적용되는지 검증
for i in range(1, N - 1):
    if arr[i+1] != arr[i] * a + b:
        print("B")
        sys.exit()

print(arr[N-1] * a + b)