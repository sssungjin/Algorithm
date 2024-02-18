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

#         7
#       10 15
#    18 11,16 15
#  20 25,23 20,19 19
# 24 25,30 27,22 26,25 24

# 0,0 -> 1,0 or 1,1
# 1,0 -> 2,0 or 2,1
# 1,1 -> 2,1 or 2,2
# 1,0 = 1,0 + 0,0

# 1,0 = 1,0 + 0,0
# 2,0 = 2,0 + 1,0

# 1,1 = 1,1 + 0,0
# 2,2 = 2,2 + 1,1
# 3,3 = 3,3 + 2,2

# 2,1 = 2,1 + 1,0 or 2,1 + 1,1
# 3,2 = 3,2 + 2,1 or 3,2 + 2,2