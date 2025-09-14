n = int(input())
info = [list(map(int, input().split())) for _ in range(6)]

# 3, 4 중에서 가장 큰 값은 높이
# 1, 2 중에서 가장 큰 값은 밑변 길이
# 3 또는 4 두번씩 반복되면

# 전체 사각형 넓이에서 작은 사각형 넓이 빼기
# 남동남 313 ㄱ 1 * 3이 작은 사각형 넓이
# 북동북 414 ㄱ 뒤집은거 4 * 1
# 북서북 424 ㄴ 2 * 4 가 작은 사각형
# 남서남 323 ㄴ 뒤집은거 3 * 2 가 작은 사각형

# 즉 가장 긴 변 양 옆에 있는 두 변의 차이가 작은 사각형의 높이 또는 너비

def check_shape():
    max_width = 0
    max_height = 0
    idx_width = 0
    idx_height = 0

    for i in range(6):
        if info[i][0] == 1 or info[i][0] == 2:
            if info[i][1] > max_width:
                max_width = info[i][1]
                idx_width = i
        else:
            if info[i][1] > max_height:
                max_height = info[i][1]
                idx_height = i

    # 작은 사각형의 변 찾기 (큰 변의 양 옆에 있는 변)
    small_w = abs(info[(idx_height - 1) % 6][1] - info[(idx_height + 1) % 6][1])
    small_h = abs(info[(idx_width - 1) % 6][1] - info[(idx_width + 1) % 6][1])

    big_area = max_width * max_height
    small_area = small_w * small_h

    return n * (big_area - small_area)
        

print(check_shape())