import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(list(map(int, input().strip())))
ans = 1

# width 는 정사각형 한 변의 길이
for width in range(1, min(n, m)):
    for i in range(n - width):
        for j in range(m - width):
            if arr[i][j] == arr[i + width][j] == arr[i + width][j + width] == arr[i][j + width]:
                ans = max(ans, (width + 1) * (width + 1))
            else:
                continue

print(ans)