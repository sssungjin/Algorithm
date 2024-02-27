# 1. 제거 2초
# 2. 설치 1초
# 높이를 동일하게 만드는 최소 시간과 높이 출력
# 최대 높이가 256이므로 브루트포스로 가능

n, m, b = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(n)]
answer = 1e9
idx = 0

for height in range(257):
    exceed_block, lack_block = 0, 0

    for i in range(n):
        for j in range(m):
            # 더 높으면 블럭에서 높이 빼서 필요 개수
            if blocks[i][j] > height:
                exceed_block += blocks[i][j] - height
            # 더 낮으면 높이에서 해당 블럭 높이 빼서 부족한 개수
            else:
                lack_block += height - blocks[i][j]
    # 현재 높이에 대해 lack_block
    if exceed_block + b >= lack_block:
        # 시간 계산
        if exceed_block * 2 + lack_block <= answer:
            answer = exceed_block * 2 + lack_block
            idx = height

print(answer, idx)
