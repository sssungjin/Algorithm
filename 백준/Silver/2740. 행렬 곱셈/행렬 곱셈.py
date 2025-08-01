import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

m2, k = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(m2)]

result = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for x in range(m):
            result[i][j] += A[i][x] * B[x][j]

for row in result:
    print(*row)