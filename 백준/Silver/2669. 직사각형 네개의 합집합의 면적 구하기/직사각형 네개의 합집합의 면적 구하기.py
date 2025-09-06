# 왼쪽 아래 x,y # 오른쪽 위 x,y

rectangle = [list(map(int, input().split())) for _ in range(4)]

graph = [[0] * (101) for _ in range(101)]

for i in range(4):
    for x in range(rectangle[i][0], rectangle[i][2]):
        for y in range(rectangle[i][1], rectangle[i][3]):
            if graph[x][y] == 0:
                graph[x][y] = 1

ans = 0
for row in graph:
    ans += sum(row)     
print(ans)