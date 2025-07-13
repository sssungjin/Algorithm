m, n = map(int, input().split())
board = [input() for _ in range(m)]
ans = []

for a in range(m - 7):
    for b in range(n - 7):
        idx1 = 0 # 맨 왼쪽위가 w
        idx2 = 0 # 맨 왼쪽위가 b
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0: # 짝수면 맨 왼쪽위와 같아야 하는데 틀리면 새로 칠함
                    if board[i][j] != 'W':
                        idx1 += 1
                    if board[i][j] != 'B':
                        idx2 += 1
                else: # 홀수면 맨 왼쪽위와 달라야함
                    if board[i][j] != 'B':
                        idx1 += 1
                    if board[i][j] != 'W':
                        idx2 += 1
        ans.append(min(idx1, idx2))

print(min(ans))