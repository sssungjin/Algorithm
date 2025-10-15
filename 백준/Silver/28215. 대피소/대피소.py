from itertools import combinations

N, K = map(int, input().split())

house = [list(map(int, input().split())) for _ in range(N)]

combis = list(combinations(house, K))
min_distance = float('inf')

def cal_distance(x1, x2, y1, y2):
    return abs(x1 - y1) + abs(x2 - y2)

for combi in combis:
    current_max_dist = 0
    for h in house:
        min_house_to_daepi = float('inf')
        min_arr = []
        # 가까운 집과 대피소와의 거리
        for daepi in combi:
            dist = cal_distance(daepi[0], daepi[1], h[0], h[1])
            min_house_to_daepi = min(dist, min_house_to_daepi)
            
        current_max_dist = max(current_max_dist, min_house_to_daepi)
    
    min_distance = min(min_distance, current_max_dist)

print(min_distance)