# 개수 최대 무게
n, k = map(int, input().split())
stuff = [[0,0]]
for i in range(n):
    stuff.append(list(map(int, input().split())))
graph = [[0 for _ in range(k+1)] for _ in range(n+1)]
    
for i in range(n+1):
    for j in range(k+1):
        weight = stuff[i][0]
        value = stuff[i][1]

        # 열의 넘버가 weight보다 작다면 위 값을 그대로 사용 0번째 행은 0이기 때문에
        # 1행에서 열의 넘버가 weight보다 작다면 0 가져옴
        if j < weight:
            graph[i][j] = graph[i - 1][j]
        # 물건을 넣고 해당 물건의 무게를 뺀 값을 더함(기존 들고 있던 거에서 뺀다)
        else:
            graph[i][j] = max(value + graph[i-1][j-weight], graph[i-1][j])

print(graph[n][k])