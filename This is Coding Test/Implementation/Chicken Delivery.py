N, M = map(int, input().split())
# 집과 치킨집의 좌표 담을 리스트
house, chicken = [], []
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 1:
            house.append([i, j])
        elif line[j] == 2:
            chicken.append([i, j])
min_val = [float("inf")]
chicken_selected = []

def check(house_list, chicken_list):
    chicken_distance = 0
    for h_i, h_j in house_list:
        tmp = float("inf")
        for c_i, c_j in chicken_list:
            tmp = min(tmp, (abs(h_i - c_i) + abs(h_j - c_j)))
        chicken_distance += tmp
    return chicken_distance

def dfs(depth, index):
    # M개의 치킨 집을 선택했다면 도시의 치킨 거리를 계산해 최소값 갱신
    if M == depth:
        min_val[0] = min(min_val[0], check(house, chicken_selected))
        return
    # 1번째 치킨집부터 끝까지, 2번째부터 끝까지, 3번째부터 끝까지.. 확인해서 최소값 구함
    for i in range(index + 1, len(chicken)):
        chicken_selected.append(chicken[i])
        dfs(depth+1, i)
        chicken_selected.remove(chicken[i])

dfs(0, -1)
print(min_val[0])