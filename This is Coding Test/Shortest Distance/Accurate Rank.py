n, m = map(int, input().split())
graph = [[int(1e9)] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = 0

# 한 학생 기준으로 성적이 모두 다 연결되어 있다면
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if graph[i][j] != int(1e9) or graph[j][i] != int(1e9):
            count += 1

    if count == n:
        result += 1

print(result)