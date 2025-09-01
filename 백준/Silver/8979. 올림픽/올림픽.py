N, K = map(int, input().split())

countries = [list(map(int, input().split())) for _ in range(N)]

countries.sort(key = lambda x: (x[1], x[2], x[3]), reverse=True)

idx = [countries[i][0] for i in range(N)].index(K)

for i in range(N):
    if countries[idx][1:] == countries[i][1:]:
        print(i + 1)
        break
