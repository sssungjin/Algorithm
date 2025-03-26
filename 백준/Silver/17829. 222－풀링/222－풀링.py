N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def pooling(n, i, j):
    if n == 2:
        values = [
            board[i][j],
            board[i][j + 1],
            board[i + 1][j],
            board[i + 1][j + 1]
        ]
        return sorted(values)[2]
    else:
        mid = n // 2
        v1 = pooling(mid, i, j)
        v2 = pooling(mid, i, j + mid)
        v3 = pooling(mid, i + mid, j)
        v4 = pooling(mid, i + mid, j + mid)
        return sorted([v1, v2, v3, v4])[2]

print(pooling(N, 0, 0))