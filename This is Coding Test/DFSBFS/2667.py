n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
num = []

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):
    # 밖으로 나가면 False
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    
    # 집이 있다면
    if graph[x][y] == 1:
        global count
        count += 1
        # 방문 처리
        graph[x][y] = 0
        # 주변에 집이 있다면 그 집 바로 확인 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

count = 0
result = 0

# 모든 좌표에 대해 dfs -> 집을 모두 지어 dfs가 끝나도 다른 단지 확인 가능
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            num.append(count)
            result += 1
            count = 0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])