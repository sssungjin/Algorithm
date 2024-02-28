n, m = map(int, input().split())

balls = [0] + list(range(1, n+1))

for _ in range(m):
    a, b = map(int, input().split())
    #change.append((a, b))
    tmp = balls[a]
    balls[a] = balls[b]
    balls[b] = tmp

for i in range(1, n+1):
    print(balls[i], end=" ")