n = int(input())
colored_paper = [tuple(map(int, input().split())) for _ in range(n)]

paper = [[0] * 100 for _ in range(100)]

for t in range(n):
    a, b = colored_paper[t]
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            paper[i][j] = 1

ans = 0

for row in paper:
    ans += sum(row)

print(ans)