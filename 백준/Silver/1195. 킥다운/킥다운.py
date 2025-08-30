g1 = input()
g2 = input()

len1 = len(g1)
len2 = len(g2)

min_len = len1 + len2

# g1을 고정하고 g2를 왼쪽부터 오른쪽으로 슬라이딩
for i in range(-len2 + 1, len1):
    is_possible = True
    for j in range(len2):
        # g2의 j번째 톱니와 매칭되는 g1의 톱니 인덱스
        g1_idx = i + j
        
        # g1의 범위를 벗어나지 않고 겹치는 부분만 확인
        if 0 <= g1_idx < len1:
            if int(g1[g1_idx]) + int(g2[j]) > 3:
                is_possible = False
                break
    
    if is_possible:
        start_idx = min(0, i)
        end_idx = max(len1, i + len2)
        current_len = end_idx - start_idx
        min_len = min(min_len, current_len)

print(min_len)