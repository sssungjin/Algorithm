tri = []
n = int(input())
for i in range(n):
    tri.append(list(map(int, input().split())))


for i in range(1, n):
     for j in range(len(tri[i])):
        # 가장 왼쪽 또는 가장 오른쪽인지 확인
        if j == 0:
            tri[i][j] += tri[i-1][j]
        elif j == (len(tri[i]) - 1):
             tri[i][j] += tri[i-1][j-1]
        else:
            tri[i][j] = max(tri[i][j] + tri[i-1][j-1], tri[i][j] + tri[i-1][j])

print(max(tri[n-1]))